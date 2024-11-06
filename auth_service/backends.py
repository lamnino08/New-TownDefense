# auth_service/backends.py

from django.contrib.auth.backends import BaseBackend
from .models import Staff
from django.contrib.auth.hashers import check_password  # Use if passwords are hashed

class StaffBackend(BaseBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            staff = Staff.objects.get(username=username)
            if staff.password == password:  # Adjust if using hashed passwords
                return staff
            else:
                return None
        except Staff.DoesNotExist:
            return None

    def get_user(self, staff_id):
        try:
            return Staff.objects.get(pk=staff_id)
        except Staff.DoesNotExist:
            return None
