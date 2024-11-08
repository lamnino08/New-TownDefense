# role_service/views.py

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Department, Role
from auth_service.models import Staff

def get_department_hierarchy(department):
    """Recursive function to build a department hierarchy with sub-departments, roles, and staffs."""
    # Fetch child departments for the current department
    child_departments = Department.objects.filter(parent=department)
    
    # Recursively build the tree for each child department
    children = [get_department_hierarchy(child) for child in child_departments]
    
    # Fetch roles for the current department
    roles = Role.objects.filter(department=department)
    
    # For each role, fetch associated staff members
    role_data = [
        {
            'role_id': role.role_id,
            'name': role.name,
            'description': role.description,
            'staffs': [
                {
                    'staff_id': staff.staff_id,
                    'name': staff.name,
                    'phone_number': staff.phone_number,
                    'username': staff.username,
                    'status': staff.status,
                    'created_at': staff.created_at,
                }
                for staff in Staff.objects.filter(role=role)
            ]
        }
        for role in roles
    ]

    # Return the current department with nested sub-departments, roles, and staff
    return {
        'department_id': department.department_id,
        'name': department.name,
        'description': department.description,
        'icon': department.icon,
        'sub_departments': children,  # Nested child departments
        'roles': role_data            # Roles with their associated staffs
    }

@api_view(['GET'])
def department_hierarchy(request):
    # Get top-level departments (those without a parent)
    root_departments = Department.objects.filter(parent__isnull=True)
    if not root_departments:
        print("No root departments found.")
    else:
        print(root_departments[0])
    # Build the hierarchy for each top-level department
    department_data = [get_department_hierarchy(department) for department in root_departments]

    return Response(department_data)

from django.http import JsonResponse
from role_service.models import Department, Role
from auth_service.models import Staff
from django.core.exceptions import ObjectDoesNotExist

def get_detail(request):
    name = request.GET.get("name")
    object_id = request.GET.get("id")
    
    if not object_id:
        return JsonResponse({'status': 'error', 'message': 'ID is required'}, status=400)

    try:
        if name == "department":
            department = Department.objects.get(department_id=object_id)
            data = {
                "department_id": department.department_id,
                "name": department.name,
                "description": department.description,
                "icon": department.icon,
                "parent_id": department.parent.department_id if department.parent else None,
                "sub_departments": [
                    {"department_id": sub.department_id, "name": sub.name} for sub in department.sub_departments.all()
                ],
                "roles": [
                    {"role_id": role.role_id, "name": role.name} for role in department.roles.all()
                ]
            }
        elif name == "role":
            role = Role.objects.get(role_id=object_id)
            data = {
                "role_id": role.role_id,
                "name": role.name,
                "description": role.description,
                "department_id": role.department.department_id if role.department else None,
                "first_page": role.first_page,
                "staffs": [
                    {"staff_id": staff.staff_id, "name": staff.name, "username": staff.username} for staff in role.staff.all()
                ]
            }
        elif name == "staff":
            staff = Staff.objects.get(staff_id=object_id)
            data = {
                "staff_id": staff.staff_id,
                "name": staff.name,
                "phone_number": staff.phone_number,
                "role_id": staff.role.role_id if staff.role else None,
                "username": staff.username,
                "status": staff.status,
                "created_at": staff.created_at,
            }
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid name parameter'}, status=400)

        return JsonResponse({"status": "success", "data": data})
    
    except ObjectDoesNotExist:
        return JsonResponse({"status": "error", "message": f"{name.capitalize()} not found"}, status=404)
