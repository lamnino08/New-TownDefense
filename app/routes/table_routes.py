from django.urls import path
from app.controllers import table_controller

urlpatterns = [
    path('table-status/', table_controller.view_table_status, name='table_status'),
    path('update-table-status/<int:table_id>/', table_controller.update_table_status, name='update_table_status'),
]
