from django.urls import path
from . import views

urlpatterns = [
    path('login/<str:username>/', views.find_by_name_login, name='find_by_name_login'),
    path('create/', views.create_staff, name='create_staff'),
    path('update/<int:id>/', views.update_staff, name='update_staff'),
    path('delete/<int:id>/', views.delete_staff, name='delete_staff'),
    path('search/', views.find_by_name, name='find_by_name'),
]
