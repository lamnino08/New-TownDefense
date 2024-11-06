from django.urls import path
from app.controllers import views  # Thay đổi theo cách bạn tổ chức controller

urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.menu_list, name='menu_list'),
    path('table-status/', views.view_table_status, name='table_status'),
    path('reserve-table/', views.reserve_table, name='reserve_table'),
    path('manage-reservations/', views.manage_reservations, name='manage_reservations'),
    path('update-reservation-status/<int:reservation_id>/', views.update_reservation_status, name='update_reservation_status'),
    path('cancel-reservation/<int:reservation_id>/', views.cancel_reservation, name='cancel_reservation'),
    path('update-table-status/<int:table_id>/', views.update_table_status, name='update_table_status'),
    path('order-dish/', views.order_dish, name='order_dish'),
    path('update-order/<int:order_id>/', views.update_dish_order, name='update_dish_order'),
    path('update-dish-status/<int:dish_id>/', views.update_dish_status, name='update_dish_status'),
    path('kitchen-orders/', views.kitchen_orders, name='kitchen_orders'),
    path('checkout/<int:bill_id>/', views.checkout, name='checkout'),
    path('bill/<int:bill_id>/', views.bill_detail, name='bill_detail'),
]
