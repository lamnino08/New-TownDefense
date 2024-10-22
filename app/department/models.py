from django.db import models

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    icon = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
