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
