from django import forms
from django.shortcuts import render

from .models import Reservation, DishOrder


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table', 'user', 'time', 'is_taken']


class DishOrderForm(forms.ModelForm):
    class Meta:
        model = DishOrder
        fields = ['bill', 'dish', 'number', 'note']


def manage_reservations(request):
    reservations = Reservation.objects.filter(is_taken=False)
    return render(request, 'reservation/manage.html', {'reservations': reservations})
