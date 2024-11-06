# auth_service/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('api/login', views.login_api, name='login_api'),
    path('logout/', views.logout_view, name='logout'),
]
