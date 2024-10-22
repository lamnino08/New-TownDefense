from django.http import JsonResponse
from .models import Department
from django.shortcuts import get_object_or_404

def get_department_by_role_id(request, roleId):
    departments = Department.objects.filter(role__role_id=roleId)
    
    department_list = list(departments.values('department_id', 'name'))
    
    return JsonResponse(department_list, safe=False)

def get_all_departments(request):
    departments = Department.objects.all()

    department_list = list(departments.values('department_id', 'name'))

    return JsonResponse(department_list, safe=False)
