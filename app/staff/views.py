from django.http import JsonResponse
from staff.services import staff_service

# Hàm xử lý lấy mật khẩu nhân viên theo username
def find_by_name_login(request, username):
    password = staff_service.get_password_by_username(username)
    if password:
        return JsonResponse({'Password': password})
    else:
        return JsonResponse({'error': 'Staff not found'}, status=404)

# Hàm xử lý tạo nhân viên mới
def create_staff(request):
    if request.method == 'POST':
        name = request.POST['Name']
        username = request.POST['username']
        role_id = request.POST['RoleID']
        phone_number = request.POST['PhoneNumber']
        password = request.POST['Password']

        staff = staff_service.create_staff(name, username, role_id, phone_number, password)
        return JsonResponse({'message': 'Staff created successfully', 'staff_id': staff.staff_id})

# Hàm xử lý cập nhật thông tin nhân viên
def update_staff(request, id):
    if request.method == 'POST':
        name = request.POST['Name']
        role_id = request.POST['RoleID']
        phone_number = request.POST['PhoneNumber']

        staff = staff_service.update_staff(id, name, role_id, phone_number)
        if staff:
            return JsonResponse({'message': 'Staff updated successfully'})
        else:
            return JsonResponse({'error': 'Staff not found'}, status=404)

# Hàm xử lý xóa nhân viên
def delete_staff(request, id):
    success = staff_service.delete_staff(id)
    if success:
        return JsonResponse({'message': 'Staff deleted successfully'})
    else:
        return JsonResponse({'error': 'Staff not found'}, status=404)

# Hàm xử lý tìm kiếm nhân viên
def find_by_name(request):
    name = request.GET.get('Name')
    department_id = request.GET.get('DepartmentID')
    role_id = request.GET.get('RoleID')

    staff_list = staff_service.search_staff(name=name, department_id=department_id, role_id=role_id)
    results = list(staff_list.values('staff_id', 'name', 'role__name', 'status', 'role__role_id', 'role__department__name', 'role__department__department_id', 'role__department__icon', 'phone_number'))
    return JsonResponse(results, safe=False)
