from django.db import models

class Department(models.Model):
    department_id = models.AutoField(primary_key=True, db_column='DepartmentID')
    name = models.TextField(db_column='Name', null=True)
    description = models.TextField(db_column='Description', null=True)
    icon = models.TextField(db_column='Icon', null=True)

    class Meta:
        db_table = 'department'
