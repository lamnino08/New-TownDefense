from django.urls import path
from app.controllers import reservation_controller

urlpatterns = [
    path('reserve-table/', reservation_controller.reserve_table, name='reserve_table'),
    path('manage-reservations/', reservation_controller.manage_reservations, name='manage_reservations'),
    path('update-reservation-status/<int:reservation_id>/', reservation_controller.update_reservation_status,
         name='update_reservation_status'),
    path('cancel-reservation/<int:reservation_id>/', reservation_controller.cancel_reservation, name='cancel_reservation'),
]
