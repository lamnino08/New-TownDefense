# auth_service/views.py
from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    # Here you can add logic for login, for now, we’ll return a simple message
    return HttpResponse("Login view for auth_service")

def logout_view(request):
    # Here you can add logic for login, for now, we’ll return a simple message
    return HttpResponse("logout view for auth_service")