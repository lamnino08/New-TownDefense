from django.shortcuts import render, redirect, get_object_or_404
from app.models.table_model import Table
from app.models.reservation_model import Reservation
from app.models.dishorder_model import DishOrder
from app.models.menu_model import Menu
from app.models.bill_model import Bill
from app.forms import ReservationForm, DishOrderForm

def index(request):
    return render(request, 'index.html')

def menu_list(request):
    menus = Menu.objects.all()
    return render(request, 'menu/menu_list.html', {'menus': menus})

def view_table_status(request):
    tables = Table.objects.all()
    return render(request, 'table/view_table_status.html', {'tables': tables})

def reserve_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('table_status')
    else:
        form = ReservationForm()
    return render(request, 'reservation/create.html', {'form': form})

def manage_reservations(request):
    reservations = Reservation.objects.filter(is_taken=False)
    return render(request, 'reservation/manage.html', {'reservations': reservations})

def update_reservation_status(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    reservation.is_taken = True
    reservation.save()
    return redirect('manage_reservations')

def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    reservation.delete()
    return redirect('manage_reservations')

def update_table_status(request, table_id):
    table = get_object_or_404(Table, pk=table_id)
    table.is_available = True
    table.save()
    return redirect('table_status')

def create_dish_order(request):
    if request.method == 'POST':
        form = DishOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = DishOrderForm()
    return render(request, 'menu/order.html', {'form': form})

def update_dish_order(request, order_id):
    order = get_object_or_404(DishOrder, pk=order_id)
    if request.method == 'POST':
        form = DishOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = DishOrderForm(instance=order)
    return render(request, 'menu/update_order.html', {'form': form})

def update_dish_status(request, dish_id):
    dish = get_object_or_404(Menu, pk=dish_id)
    if request.method == 'POST':
        dish.is_available = False
        dish.save()
    return redirect('kitchen_orders')

def kitchen_orders(request):
    dish_orders = DishOrder.objects.all()
    return render(request, 'kitchen/update_status.html', {'dish_orders': dish_orders})

def checkout(request, bill_id):
    bill = get_object_or_404(Bill, pk=bill_id)
    bill.is_payed = True
    bill.save()
    return redirect('bill_detail', bill_id=bill.bill_id)

def bill_detail(request, bill_id):
    bill = get_object_or_404(Bill, pk=bill_id)
    return render(request, 'bill/detail.html', {'bill': bill})

def order_dish(request):
    if request.method == 'POST':
        dish_id = request.POST.get('dish_id')
        quantity = request.POST.get('quantity')
        note = request.POST.get('note', '')

        bill_id = request.POST.get('bill_id')
        bill = get_object_or_404(Bill, pk=bill_id)
        dish = get_object_or_404(Menu, pk=dish_id)

        dish_order = DishOrder(bill=bill, dish=dish, number=quantity, note=note)
        dish_order.save()

        return redirect('order_dish')

    dishes = Menu.objects.filter(is_available=True)
    return render(request, 'order_dish.html', {'dishes': dishes})
