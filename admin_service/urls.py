# auth_service/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('get-view/', views.get_view_dashboard, name='get_view'),
    path('api/filter-staff/', views.filter_staff, name='get_panel'),
    path('api/add_staff/', views.create_staff_api, name='add_staff'),
    path('api/update-staff/<int:staff_id>/', views.edit_staff_api, name='edit_staff'),
    path('api/get-staff/<int:staff_id>/', views.get_staff_api, name='get_a_staff'),
    path('api/update-status-staff/<int:staff_id>/', views.update_status_staff, name='update_status'),
    path('api/delete-staff/<int:staff_id>/', views.delete_staff, name='delete_staff'),
]
