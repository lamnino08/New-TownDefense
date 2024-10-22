from django.urls import path
from app.controllers import menu_controller

urlpatterns = [
    path('menu/', menu_controller.menu_list, name='menu_list'),
    path('create-order/', menu_controller.create_dish_order, name='create_dish_order'),
    path('update-order/<int:order_id>/', menu_controller.update_dish_order, name='update_dish_order'),
]
