# role_service/urls.py
from django.urls import path
from .views import department_hierarchy, get_detail

urlpatterns = [
    path('api/structure/', department_hierarchy, name='department_hierarchy'),
    path('api/get-detail/', get_detail, name='department_hierarchy'),
]
