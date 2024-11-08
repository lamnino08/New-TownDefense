# auth_service/service.py

from auth_service.models import Staff, Role, Department
from rest_framework.exceptions import NotFound

def get_staff_data():
    staff_list = Staff.objects.select_related('role__department').all()
    staff_data = [
        {
            "StaffID": staff.staff_id,
            "Name": staff.name,
            "PhoneNumber": staff.phone_number,
            "Role": {
                "RoleID": staff.role.role_id,
                "Name": staff.role.name,
                "Description": staff.role.description,
                "FirstPage": staff.role.first_page,
                "Department": {
                    "DepartmentID": staff.role.department.department_id if staff.role.department else None,
                    "Name": staff.role.department.name if staff.role.department else None,
                    "Description": staff.role.department.description if staff.role.department else None,
                    "Icon": staff.role.department.icon if staff.role.department else None,
                }
            },
            "Status": staff.status,
            "CreateAt": staff.created_at,
            "Username": staff.username,
        }
        for staff in staff_list
    ]
    return staff_data

def get_a_staff_data(staff_id):
    staff = Staff.objects.select_related('role__department').filter(staff_id=staff_id).first()  # Chỉ lấy một nhân viên đầu tiên

    if not staff:  # Nếu không tìm thấy nhân viên
        return {'status': 'error', 'message': 'Staff not found'}

    staff_data = {
        "StaffID": staff.staff_id,
        "Name": staff.name,
        "PhoneNumber": staff.phone_number,
        "Role": {
            "RoleID": staff.role.role_id,
            "Name": staff.role.name,
            "Description": staff.role.description,
            "FirstPage": staff.role.first_page,
            "Department": {
                "DepartmentID": staff.role.department.department_id if staff.role.department else None,
                "Name": staff.role.department.name if staff.role.department else None,
                "Description": staff.role.department.description if staff.role.department else None,
                "Icon": staff.role.department.icon if staff.role.department else None,
            }
        },
        "Password": staff.password,
        "Status": staff.status,
        "CreateAt": staff.created_at,
        "Username": staff.username,
    }

    return {'status': 'success', 'data': staff_data}

def get_roles_data():
    roles = Role.objects.all()
    return [
        {
            "RoleID": role.role_id,
            "Name": role.name,
            "Description": role.description,
            "FirstPage": role.first_page,
            "DepartmentID": role.department_id
        }
        for role in roles
    ]

def get_departments_data():
    departments = Department.objects.all()
    return [
        {
            "DepartmentID": department.department_id,
            "Name": department.name,
            "Description": department.description,
            "Icon": department.icon
        }
        for department in departments
    ]

def get_filtered_staff(name=None, department=None, role=None):
    """
    Service function to filter staff based on name, department, and role.
    """
    staff_query = Staff.objects.select_related('role', 'role__department').all()
    
    if name:
        staff_query = staff_query.filter(name__icontains=name)
    if department:
        staff_query = staff_query.filter(role__department__department_id=department)
    if role:
        staff_query = staff_query.filter(role__role_id=role)
    
    return [
        {
            "StaffID": staff.staff_id,
            "Name": staff.name,
            "PhoneNumber": staff.phone_number,
            "Role": {
                "RoleID": staff.role.role_id,
                "Name": staff.role.name,
                "Department": {
                    "DepartmentID": staff.role.department.department_id if staff.role.department else None,
                    "Name": staff.role.department.name if staff.role.department else None,
                    "Description": staff.role.department.description if staff.role.department else None,
                    "Icon": staff.role.department.icon if staff.role.department else None,
                } if staff.role else None
            },
            "Status": staff.status,
            "Username": staff.username,
        }
        for staff in staff_query
    ]
    
def create_staff_account(data):
    """
    Create a new staff account with the provided data.
    """
    try:
        staff = Staff(
            name=data.get("name"),
            username=data.get("username"),
            phone_number=data.get("phone"),
            role=data.get("roleId"),
            password=data.get("password"),  
        )
        staff.save()
        return {"status": "success", "message": "Staff account created successfully."}
    except Role.DoesNotExist:
        return {"status": "error", "message": "Invalid role ID."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
def update_staff(staff_id, data):
    try:
        staff = Staff.objects.get(staff_id=staff_id) 
    except Staff.DoesNotExist:
        raise NotFound("Staff member not found.") 

    role = None
    if 'role_id' in data:
        try:
            role = Role.objects.get(role_id=int(data['role_id']))  
        except Role.DoesNotExist:
            raise NotFound("Role not found.")  
    staff.username = data.get('username', staff.username) 
    staff.name = data.get('name', staff.name) 
    staff.phone_number = data.get('phone', staff.phone_number)  
    staff.role = role if role else staff.role  
    staff.password = data.get('password', staff.password)  

    staff.save()
    staff_data = {"StaffID": staff.staff_id,
            "Name": staff.name,
            "PhoneNumber": staff.phone_number,
            "Role": {
                "RoleID": staff.role.role_id,
                "Name": staff.role.name,
                "Department": {
                    "DepartmentID": staff.role.department.department_id if staff.role.department else None,
                    "Name": staff.role.department.name if staff.role.department else None,
                    "Description": staff.role.department.description if staff.role.department else None,
                    "Icon": staff.role.department.icon if staff.role.department else None,
                } if staff.role else None
            },
            "Status": staff.status,
            "Username": staff.username,
    }
    return staff_data


def update_staff_status(staff_id, new_status):
    try:
        staff = Staff.objects.get(staff_id=staff_id)
        staff.status = new_status
        staff.save()
        return {'status': 'success'}
    except NotFound:
        return {'status': 'error', 'message': 'Staff not found'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}
    
def delete_a_staff(staff_id):
    try:
        staff = Staff.objects.get(staff_id=staff_id)

        staff.delete()

        return {'status': 'success', 'message': 'Staff member deleted successfully'}
    
    except Staff.DoesNotExist:
        return {'status': 'error', 'message': 'Staff member not found'}
    
    except Exception as e:
        return {'status': 'error', 'message': str(e)}
