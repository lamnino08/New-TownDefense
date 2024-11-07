from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_all_tables, name='view_all_tables'),
    path('reserve/<int:table_id>/', views.reserve_table_online,
         name='reserve_table_online'),
    path('cancel/<int:table_id>/', views.cancel_reservation,
         name='cancel_reservation'),
    path('update-status/<int:table_id>/<str:status>/',
         views.update_table_status, name='update_table_status'),
    path('order/<int:table_id>/', views.order_food, name='order_food'),
    path('update-order/<int:order_id>/<str:status>/',
         views.update_order_status, name='update_order_status'),
    path('orders/<int:table_id>/', views.view_orders, name='view_orders'),
]
