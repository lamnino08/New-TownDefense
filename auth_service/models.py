# auth_service/models.py
from django.db import models
from role_service.models import Role, Department

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True, db_column='StaffID')
    name = models.TextField(null=True, blank=True, db_column='Name')
    phone_number = models.TextField(db_column='PhoneNumber')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, db_column='RoleID', related_name='staff')  # ForeignKey to Role
    password = models.TextField(null=True, blank=True, db_column='Password')
    status = models.BooleanField(default=True, db_column='Status')
    created_at = models.DateTimeField(null=True, blank=True, db_column='CreateAt')
    username = models.TextField(unique=True, db_column='username')

    class Meta:
        db_table = 'staff'

    def __str__(self):
        return self.username
