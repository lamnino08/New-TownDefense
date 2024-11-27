from django.urls import path
from . import views  # Import views từ hr_service

urlpatterns = [
    path('employee_work_history/', views.employee_work_history, name='employee_work_history'),
    path('shifts/', views.shift_list, name='shift_list'),
    path('shifts/register/', views.register_shift, name='register_shift'),
    path('create_shift/', views.create_shift, name='create_shift'),
    path('check_in/', views.check_in, name='check_in'),
    path('check_out/', views.check_out, name='check_out'),
    path('salaries/', views.salary_list, name='salary_list'),
    path('salaries/<int:salary_id>/edit/', views.edit_salary, name='edit_salary'),
    path('salaries/calculate/', views.calculate_salary_view, name='calculate_salary_view'),
]
