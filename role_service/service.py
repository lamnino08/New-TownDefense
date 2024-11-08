from role_service.models import Department, Role
from auth_service.models import Staff
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

def get_department_by_id(department_id):
    """Fetch a Department object by its ID and return as JSON"""
    try:
        department = Department.objects.get(department_id=department_id)
        data = {
            "department_id": department.department_id,
            "name": department.name,
            "description": department.description,
            "icon": department.icon,
            "parent_id": department.parent.department_id if department.parent else None,
        }
        return JsonResponse({"status": "success", "data": data})
    except ObjectDoesNotExist:
        return JsonResponse({"status": "error", "message": "Department not found"}, status=404)

def get_role_by_id(role_id):
    """Fetch a Role object by its ID and return as JSON"""
    try:
        role = Role.objects.get(role_id=role_id)
        data = {
            "role_id": role.role_id,
            "name": role.name,
            "description": role.description,
            "department_id": role.department.department_id if role.department else None,
            "first_page": role.first_page,
        }
        return JsonResponse({"status": "success", "data": data})
    except ObjectDoesNotExist:
        return JsonResponse({"status": "error", "message": "Role not found"}, status=404)

def get_staff_by_id(staff_id):
    """Fetch a Staff object by its ID and return as JSON"""
    try:
        staff = Staff.objects.get(staff_id=staff_id)
        data = {
            "staff_id": staff.staff_id,
            "name": staff.name,
            "phone_number": staff.phone_number,
            "role_id": staff.role.role_id if staff.role else None,
            "username": staff.username,
            "status": staff.status,
            "created_at": staff.created_at,
        }
        return JsonResponse({"status": "success", "data": data})
    except ObjectDoesNotExist:
        return JsonResponse({"status": "error", "message": "Staff not found"}, status=404)
