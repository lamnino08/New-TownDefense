from staff.models import Staff
from django.core.exceptions import ObjectDoesNotExist

# Hàm lấy mật khẩu nhân viên theo username
def get_password_by_username(username):
    try:
        staff = Staff.objects.get(username=username)
        return staff.password
    except ObjectDoesNotExist:
        return None

# Hàm tạo nhân viên mới
def create_staff(name, username, role_id, phone_number, password):
    staff = Staff.objects.create(
        name=name,
        username=username,
        role_id=role_id,
        phone_number=phone_number,
        password=password
    )
    return staff

# Hàm cập nhật thông tin nhân viên
def update_staff(staff_id, name, role_id, phone_number):
    try:
        staff = Staff.objects.get(pk=staff_id)
        staff.name = name
        staff.role_id = role_id
        staff.phone_number = phone_number
        staff.save()
        return staff
    except Staff.DoesNotExist:
        return None

# Hàm xóa nhân viên
def delete_staff(staff_id):
    try:
        staff = Staff.objects.get(pk=staff_id)
        staff.delete()
        return True
    except Staff.DoesNotExist:
        return False

# Hàm tìm kiếm nhân viên
def search_staff(name=None, department_id=None, role_id=None):
    query = Staff.objects.select_related('role__department').all()
    
    if name:
        query = query.filter(name__icontains=name)
    if department_id:
        query = query.filter(role__department__department_id=department_id)
    if role_id:
        query = query.filter(role__role_id=role_id)

    return query
