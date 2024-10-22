from django.urls import path
from app.controllers import dish_controller

urlpatterns = [
    path('order-dish/', dish_controller.order_dish, name='order_dish'),
]
