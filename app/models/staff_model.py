from django.db import models
from .role_model import Role

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True, db_column='StaffID')
    name = models.TextField(db_column='Name', null=True)
    phone_number = models.TextField(db_column='PhoneNumber', null=False)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, db_column='RoleID', null=True)
    password = models.TextField(db_column='Password', null=True)
    create_at = models.DateTimeField(db_column='CreateAt', null=True)
    username = models.TextField(db_column='Username', null=True)

    class Meta:
        db_table = 'staff'
