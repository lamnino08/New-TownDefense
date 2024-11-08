# role_service/models.py

from django.db import models

class Department(models.Model):
    department_id = models.AutoField(primary_key=True, db_column='DepartmentID')
    name = models.TextField(null=True, blank=True, db_column='Name')
    description = models.TextField(null=True, blank=True, db_column='Description')
    icon = models.TextField(null=True, blank=True, db_column='Icon')
    parent = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        db_column='ParentID', 
        related_name='sub_departments'
    )

    class Meta:
        db_table = 'department'  
        managed = True

    def __str__(self):
        return self.name or "Unnamed Department"


class Role(models.Model):
    role_id = models.AutoField(primary_key=True, db_column='RoleID')
    name = models.TextField(db_column='Name')
    description = models.TextField(db_column='Description', null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, db_column='DepartmentID', related_name='roles')
    first_page = models.TextField(null=True, blank=True, db_column='FirstPage')
    class Meta:
        db_table = 'role'

    def __str__(self):
        return self.name
