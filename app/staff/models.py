from django.db import models
from role.models import Role

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    status = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    # Hàm để lấy mật khẩu của nhân viên theo username
    @classmethod
    def get_password_by_username(cls, username):
        try:
            return cls.objects.get(username=username).password
        except cls.DoesNotExist:
            return None

    # Hàm để tìm kiếm nhân viên
    @classmethod
    def search_staff(cls, name=None, department_id=None, role_id=None):
        query = cls.objects.select_related('role__department').all()
        if name:
            query = query.filter(name__icontains=name)
        if department_id:
            query = query.filter(role__department__department_id=department_id)
        if role_id:
            query = query.filter(role__role_id=role_id)
        return query
