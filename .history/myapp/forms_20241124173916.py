from django import forms
from django.contrib import admin
from .models import Bill, Order, Profile, BillDish


class OrderForm(forms.ModelForm):
    customer = forms.ModelChoiceField(
        queryset=Profile.objects.all(), required=True)

    class Meta:
        model = Order
        fields = ['customer', 'item', 'invoice_id']


class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['table', 'customer', 'dishes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'table' in kwargs.get('initial', {}):
            self.fields['table'].initial = kwargs.get('initial').get('table')


class BillDishForm(forms.ModelForm):
    class Meta:
        model = BillDish
        fields = ['bill', 'dish', 'quantity', 'note']
