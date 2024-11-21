# auth_service/urls.py
from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),
    path('calendar/', views.calendar, name='calendar_list'),
    path('timeline/', views.timeline, name='timeline_list'),
    path('hr/edit/<int:employee_id>/', views.employee_edit, name='employee_edit'),
]




