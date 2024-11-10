
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_inventory, name='home'),
    path('materials/', views.materials, name='materials'),
   
    path('home/delete/<int:supplier_id>/', views.delete_supplier, name='delete_supplier'),  # Add this line

    
]
