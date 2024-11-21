from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('profile_picture', 'phone_number', 'date_of_birth', 'gender', 'address')}),
    )
    list_display = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'gender']
