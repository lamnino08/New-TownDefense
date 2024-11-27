from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .form import ShiftForm, AttendanceForm, ShiftRegistrationForm, SalaryForm
from .models import CustomUser, WorkHistory, Attendance, Shift, Salary
from django.http import JsonResponse
from datetime import datetime, timedelta, date
from django.db.models import Sum, Count




def add_shift(request):
    if request.method == 'POST':
        form = ShiftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shift_list')  # Redirect tới danh sách ca làm việc (hoặc trang khác)
    else:
        form = ShiftForm()
    return render(request, 'hr_service/add_shift.html', {'form': form})

def register_shift(request):
    """
    Nhân viên đăng ký ca làm việc.
    """
    if request.method == 'POST':
        form = ShiftRegistrationForm(request.POST)
        if form.is_valid():
            shift_id = form.cleaned_data['shift_id']
            shift = get_object_or_404(Shift, id=shift_id)

            if shift.remaining_slots() > 0:  # Kiểm tra còn chỗ
                if request.user not in shift.registered_employees.all():
                    shift.registered_employees.add(request.user)
                    shift.save()
                    return JsonResponse({"status": "success", "message": "Đăng ký thành công!"})
                else:
                    return JsonResponse({"status": "error", "message": "Bạn đã đăng ký ca này."})
            else:
                return JsonResponse({"status": "error", "message": "Ca làm việc đã đủ nhân viên."})
        else:
            return JsonResponse({"status": "error", "message": "Dữ liệu không hợp lệ."})

    return JsonResponse({"status": "error", "message": "Chỉ hỗ trợ POST request."})

def employee_info_view(request, user_ids):
    """
    Hiển thị thông tin nhân viên được chọn trong bảng.
    """
    ids = user_ids.split(",")  # Tách danh sách các ID từ chuỗi
    users = CustomUser.objects.filter(id__in=ids)  # Lấy danh sách nhân viên từ ID
    return render(request, 'employee_info.html', {'users': users})



def employee_work_history(request):
    """
    Hiển thị lịch sử làm việc của tất cả nhân viên.
    """
    users = CustomUser.objects.all()  # Lấy danh sách tất cả nhân viên
    return render(request, 'employee_work_history.html', {'users': users})


def shift_list(request):
    """
    Hiển thị danh sách ca làm việc.
    """
    shifts = Shift.objects.all()
    return render(request, 'shift_list.html', {'shifts': shifts})

def create_shift(request):
    """
    Admin tạo ca làm việc mới.
    """
    if request.method == 'POST':
        form = ShiftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shift_list')
    else:
        form = ShiftForm()

    return render(request, 'create_shift.html', {'form': form})

def check_in(request):
    """
    Nhân viên thực hiện check-in cho ca làm việc.
    """
    if request.method == 'POST':
        shift_id = request.POST.get('shift_id')
        shift = get_object_or_404(Shift, id=shift_id)

        # Kiểm tra nhân viên đã đăng ký ca này chưa
        if request.user in shift.registered_employees.all():
            attendance, created = Attendance.objects.get_or_create(employee=request.user, shift=shift, date=datetime.today().date())

            if not attendance.check_in:
                attendance.check_in = datetime.now().time()
                attendance.save()
                return JsonResponse({"status": "success", "message": "Check-in thành công!"})
            else:
                return JsonResponse({"status": "error", "message": "Bạn đã check-in rồi!"})
        else:
            return JsonResponse({"status": "error", "message": "Bạn chưa đăng ký ca này."})

    shifts = Shift.objects.filter(registered_employees=request.user)
    return render(request, 'check_in.html', {'shifts': shifts})

def check_out(request):
    """
    Nhân viên thực hiện check-out cho ca làm việc.
    """
    if request.method == 'POST':
        shift_id = request.POST.get('shift_id')
        shift = get_object_or_404(Shift, id=shift_id)

        try:
            attendance = Attendance.objects.get(employee=request.user, shift=shift, date=datetime.today().date())

            if not attendance.check_out:
                attendance.check_out = datetime.now().time()
                attendance.save()
                return JsonResponse({"status": "success", "message": "Check-out thành công!"})
            else:
                return JsonResponse({"status": "error", "message": "Bạn đã check-out rồi!"})
        except Attendance.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Bạn chưa check-in cho ca này."})

    shifts = Shift.objects.filter(registered_employees=request.user)
    return render(request, 'check_out.html', {'shifts': shifts})

def salary_list(request):
    """
    Hiển thị danh sách bảng lương.
    """
    if request.user.is_superuser:
        # Admin xem tất cả bảng lương
        salaries = Salary.objects.all()
    else:
        # Nhân viên chỉ xem bảng lương của mình
        salaries = Salary.objects.filter(employee=request.user)

    return render(request, 'salary_list.html', {'salaries': salaries})

def edit_salary(request, salary_id):
    """
    Chỉnh sửa lương cơ bản của một nhân viên (chỉ dành cho admin).
    """
    if not request.user.is_superuser:
        return redirect('salary_list')  # Chuyển hướng nếu không phải admin

    salary = get_object_or_404(Salary, id=salary_id)
    if request.method == 'POST':
        form = SalaryForm(request.POST, instance=salary)
        if form.is_valid():
            form.save()
            salary.calculate_salary()  # Cập nhật tổng lương sau khi thay đổi
            return redirect('salary_list')
    else:
        form = SalaryForm(instance=salary)

    return render(request, 'edit_salary.html', {'form': form, 'salary': salary})

def calculate_salary_view(request):
    """
    Tính toán lương cho tất cả nhân viên (chỉ admin thực hiện).
    """
    if not request.user.is_superuser:
        return redirect('salary_list')  # Chuyển hướng nếu không phải admin

    today = date.today()
    start_of_month = today.replace(day=1)

    # Lấy model người dùng
    User = get_user_model()

    # Duyệt qua từng nhân viên và tính lương
    for employee in User.objects.all():
        salary, created = Salary.objects.get_or_create(employee=employee, month=start_of_month)
        salary.calculate_salary()  # Hàm tính toán lương đã được định nghĩa trong model

    return redirect('salary_list')