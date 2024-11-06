from django.urls import path
from app.controllers import kitchen_controller

urlpatterns = [
    path('kitchen-orders/', kitchen_controller.kitchen_orders, name='kitchen_orders'),
    path('update-dish-status/<int:dish_id>/', kitchen_controller.update_dish_status, name='update_dish_status'),
]
