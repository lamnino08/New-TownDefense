from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.conf import settings
from datetime import datetime, time, timedelta  

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Đặt related_name duy nhất
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',  # Đặt related_name duy nhất
        blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

class Shift(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    shift_type = models.CharField(
        max_length=50,
        choices=[
            ('morning', 'Morning'),
            ('afternoon', 'Afternoon'),
            ('night', 'Night'),
        ],
        default='morning'
    )
    salary_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=1.00,
        help_text="Tỷ lệ lương so với mức cơ bản (ví dụ: 1.5 = tăng 50%)."
    )
    notes = models.TextField(blank=True, null=True)
    max_employees = models.PositiveIntegerField(default=10, verbose_name="Số nhân viên tối đa")
    registered_employees = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='registered_shifts',
        blank=True,
        verbose_name="Nhân viên đã đăng ký"
    )

    def __str__(self):
        return f"{self.shift_type} ({self.start_time} - {self.end_time})"

    def remaining_slots(self):
        return self.max_employees - self.registered_employees.count()



class WorkHistory(models.Model):
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='work_histories'
    )
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # Có thể để trống
    kpi = models.IntegerField(default=0, help_text="Hiệu suất làm việc (KPI 0-100)")
    contract_type = models.CharField(
        max_length=50,
        choices=[
            ('full_time', 'Full-time'),
            ('part_time', 'Part-time'),
            ('contract', 'Contract'),
        ],
        default='full_time'
    )
    contract_duration = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.employee} ({self.start_date} - {self.end_date or 'Present'})"
    
class Attendance(models.Model):
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="attendances",
        verbose_name="Nhân viên"
    )
    shift = models.ForeignKey(
        'Shift',  # Liên kết với ca làm việc
        on_delete=models.CASCADE,
        related_name="attendances",
        verbose_name="Ca làm việc"
    )
    date = models.DateField(auto_now_add=True, verbose_name="Ngày chấm công")
    check_in = models.TimeField(blank=True, null=True, verbose_name="Giờ vào")
    check_out = models.TimeField(blank=True, null=True, verbose_name="Giờ ra")
    is_late = models.BooleanField(default=False, verbose_name="Đi muộn")
    early_leave = models.BooleanField(default=False, verbose_name="Về sớm")

    def __str__(self):
        return f"{self.employee.username} - {self.shift} ({self.date})"

    def calculate_total_hours(self):
        """
        Tính tổng số giờ làm việc trong ngày.
        """
        if self.check_in and self.check_out:
            check_in_time = datetime.combine(self.date, self.check_in)
            check_out_time = datetime.combine(self.date, self.check_out)
            delta = check_out_time - check_in_time
            return delta.total_seconds() / 3600  # Trả về số giờ làm việc
        return 0

    def save(self, *args, **kwargs):
        """
        Ghi đè phương thức save để tự động tính trạng thái đi muộn hoặc về sớm dựa trên ca làm việc.
        """
        if self.shift:
            work_start_time = self.shift.start_time.time()
            work_end_time = self.shift.end_time.time()

            # Xác định trạng thái đi muộn
            if self.check_in and self.check_in > work_start_time:
                self.is_late = True
            else:
                self.is_late = False

            # Xác định trạng thái về sớm
            if self.check_out and self.check_out < work_end_time:
                self.early_leave = True
            else:
                self.early_leave = False

        super().save(*args, **kwargs)  # Lưu đối tượng

class Salary(models.Model):
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="salaries",
        verbose_name="Nhân viên"
    )
    month = models.CharField(
        max_length=7,  # Chỉ lưu tháng và năm, ví dụ: "11/2024"
        verbose_name="Tháng/Năm"
    )
    total_shifts = models.PositiveIntegerField(default=0, verbose_name="Tổng số ca làm việc")
    base_salary = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        default=0,
        verbose_name="Lương cơ bản mỗi ca (VNĐ)"
    )
    total_salary = models.DecimalField(
        max_digits=12,
        decimal_places=0,
        default=0,
        verbose_name="Tổng lương (VNĐ)"
    )

    def __str__(self):
        return f"Lương của {self.employee.username} - {self.month}"

    def calculate_salary(self):
        """
        Tự động tính tổng lương dựa trên số ca làm việc và lương cơ bản mỗi ca.
        """
        # Lấy danh sách các ca làm việc của nhân viên trong tháng
        start_of_month = date(int(self.month.split('/')[1]), int(self.month.split('/')[0]), 1)
        end_of_month = (start_of_month.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)

        shifts = self.employee.registered_shifts.filter(
            start_time__date__gte=start_of_month,
            start_time__date__lte=end_of_month
        )

        # Cập nhật số ca làm việc
        self.total_shifts = shifts.count()

        # Tính tổng lương
        self.total_salary = self.total_shifts * self.base_salary
        self.save()