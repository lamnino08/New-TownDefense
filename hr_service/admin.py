from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import CustomUser, Shift, Attendance, WorkHistory, Salary
from django.utils.html import format_html
from django.urls import reverse, path, reverse 
from django.shortcuts import render  




@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'view_employee_info_link']
    actions = ['view_employee_info']

    def get_urls(self):
        """
        Thêm URL tùy chỉnh để hiển thị thông tin nhân viên.
        """
        urls = super().get_urls()
        custom_urls = [
            path('employee_info/<str:user_ids>/', self.admin_site.admin_view(self.employee_info_view), name='employee_info'),
        ]
        return custom_urls + urls

    def employee_info_view(self, request, user_ids):
        """
        View hiển thị bảng thông tin nhân viên.
        """
        ids = user_ids.split(",")  # Tách danh sách ID
        users = CustomUser.objects.filter(id__in=ids)  # Lấy danh sách nhân viên từ ID
        return render(request, 'hr_service/employee_info.html', {'users': users})


    def view_employee_info_link(self, obj):
        """
        Thêm liên kết trong danh sách Admin.
        """
        url = reverse('admin:employee_info', args=[obj.id])
        return format_html(f'<a href="{url}">Xem thông tin</a>')

    view_employee_info_link.short_description = "Thông tin nhân viên"

    def view_employee_info(self, request, queryset):
        """
        Action hiển thị thông tin nhân viên qua URL tùy chỉnh.
        """
        if not queryset.exists():
            self.message_user(request, "Không có nhân viên nào được chọn.")
            return

        user_ids = ",".join(str(user.id) for user in queryset)  # Lấy danh sách ID
        return HttpResponseRedirect(reverse('admin:employee_info', args=[user_ids]))
    
    def view_work_history_link(self, obj):
        url = reverse('employee_work_history', args=[obj.id])
        return format_html(f'<a href="{url}">Xem lịch sử làm việc</a>')

    view_work_history_link.short_description = "Lịch sử làm việc"
            

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('shift_type', 'start_time', 'end_time', 'max_employees', 'remaining_slots')
    list_filter = ('shift_type', 'start_time', 'end_time')
    search_fields = ('shift_type',)

    def has_add_permission(self, request):
        """
        Chỉ admin mới có quyền thêm ca.
        """
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        """
        Chỉ admin mới có quyền chỉnh sửa ca.
        """
        return request.user.is_superuser

@admin.register(WorkHistory)
class WorkHistoryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'start_date', 'end_date', 'kpi', 'contract_type', 'contract_duration')
    list_filter = ('contract_type', 'start_date', 'end_date')
    search_fields = ('employee__username', 'contract_type')

@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'month', 'total_shifts', 'base_salary', 'total_salary')
    list_filter = ('month',)
    search_fields = ('employee__username', 'employee__email')

    def save_model(self, request, obj, form, change):
        """
        Tự động tính lại lương sau khi admin chỉnh sửa.
        """
        super().save_model(request, obj, form, change)
        obj.calculate_salary()  # Gọi hàm tính lương trong model

    