from django.urls import path
from . import views

urlpatterns = [
    path('getDepartmentByRole/<int:roleId>/', views.get_department_by_role_id, name='get_department_by_role'),
    path('getAllDepartments/', views.get_all_departments, name='get_all_departments'),
]
