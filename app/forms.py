from django import forms
from .models import Reservation, DishOrder

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table', 'user', 'time', 'is_taken']

class DishOrderForm(forms.ModelForm):
    class Meta:
        model = DishOrder
        fields = ['bill', 'dish', 'number', 'note']
