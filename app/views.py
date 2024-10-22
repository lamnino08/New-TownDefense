from django.shortcuts import render, redirect, get_object_or_404
from .models import Table, Reservation, DishOrder, Menu, Bill
from .forms import ReservationForm, DishOrderForm


def menu_list(request):
    menus = Menu.objects.all()  # Lấy tất cả các món ăn từ bảng Menu
    return render(request, 'menu/menu_list.html', {'menus': menus})


def index(request):
    return render(request, 'index.html')


def view_table_status(request):
    tables = Table.objects.all()
    context = {
        'tables': tables
    }
    return render(request, 'table/view_table_status.html', context)


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
    reservation = Reservation.objects.get(pk=reservation_id)
    reservation.is_taken = True
    reservation.save()
    return redirect('manage_reservations')


def cancel_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    reservation.delete()
    return redirect('manage_reservations')


def update_table_status(request, table_id):
    table = Table.objects.get(pk=table_id)
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
    order = DishOrder.objects.get(pk=order_id)
    if request.method == 'POST':
        form = DishOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = DishOrderForm(instance=order)
    return render(request, 'menu/update_order.html', {'form': form})


def update_dish_status(request, dish_id):
    dish = Menu.objects.get(pk=dish_id)
    if request.method == 'POST':
        dish.is_available = False
        dish.save()
    return redirect('kitchen_orders')


def kitchen_orders(request):
    # Lấy danh sách tất cả các đơn đặt món từ bếp
    dish_orders = DishOrder.objects.all()

    # Trả về trang HTML với danh sách các đơn đặt món
    return render(request, 'kitchen/update_status.html', {'dish_orders': dish_orders})


def checkout(request, bill_id):
    bill = Bill.objects.get(bill_id=bill_id)
    bill.is_payed = True
    bill.save()
    return redirect('bill_detail', bill_id=bill.bill_id)


def bill_detail(request, bill_id):
    bill = get_object_or_404(Bill, bill_id=bill_id)
    return render(request, 'bill/detail.html', {'bill': bill})


def order_dish(request):
    if request.method == 'POST':
        # Lấy thông tin từ form gọi món
        dish_id = request.POST.get('dish_id')
        quantity = request.POST.get('quantity')
        note = request.POST.get('note', '')

        # Lưu thông tin vào database (giả sử đang xử lý cho bàn cụ thể, bạn có thể điều chỉnh)
        bill_id = request.POST.get('bill_id')  # Giả sử bạn có bill_id từ request
        bill = Bill.objects.get(pk=bill_id)
        dish = Menu.objects.get(pk=dish_id)

        # Tạo DishOrder mới
        dish_order = DishOrder(bill=bill, dish=dish, number=quantity, note=note)
        dish_order.save()

        # Sau khi gọi món thành công, có thể chuyển hướng hoặc hiển thị thông báo
        return redirect('order_dish')

    # Hiển thị danh sách món ăn để nhân viên phục vụ chọn
    dishes = Menu.objects.filter(is_available=True)
    return render(request, 'order_dish.html', {'dishes': dishes})
