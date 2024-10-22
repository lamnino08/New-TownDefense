from django.urls import path
from app.controllers import bill_controller

urlpatterns = [
    path('checkout/<int:bill_id>/', bill_controller.checkout, name='checkout'),
    path('bill/<int:bill_id>/', bill_controller.bill_detail, name='bill_detail'),
]
