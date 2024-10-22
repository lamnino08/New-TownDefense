from django.db import models
from .department_model import Department

class Role(models.Model):
    role_id = models.AutoField(primary_key=True, db_column='RoleID')
    name = models.TextField(db_column='Name', null=True)
    description = models.TextField(db_column='Description', null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, db_column='DepartmentID', null=True)

    class Meta:
        db_table = 'role'
