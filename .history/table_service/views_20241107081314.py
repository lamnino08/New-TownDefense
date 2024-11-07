from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from .service import TableService, OrderService

# Xem danh sách bàn và trạng thái bàn


def view_all_tables(request):
    tables = TableService.get_all_tables()
    return render(request, 'restaurant_management/table_service/templates/table/view_table_status.html', {'tables': tables})

# Đặt bàn trực tuyến


def reserve_table_online(request, table_id):
    try:
        TableService.reserve_table(table_id)
        return redirect('view_all_tables')
    except Exception as e:
        return HttpResponseBadRequest(f"Lỗi đặt bàn: {str(e)}")

# Hủy đặt bàn


def cancel_reservation(request, table_id):
    try:
        TableService.cancel_reservation(table_id)
        return redirect('view_all_tables')
    except Exception as e:
        return HttpResponseBadRequest(f"Lỗi hủy đặt bàn: {str(e)}")

# Cập nhật trạng thái bàn


def update_table_status(request, table_id, status):
    try:
        TableService.update_table_status(table_id, status)
        return redirect('view_all_tables')
    except Exception as e:
        return HttpResponseBadRequest(f"Lỗi cập nhật trạng thái bàn: {str(e)}")

# Gọi món ăn


def order_food(request, table_id):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        quantity = int(request.POST.get('quantity'))
        note = request.POST.get('note', "")
        OrderService.create_order(table_id, item_name, quantity, note)
        return redirect('view_orders', table_id=table_id)
    return render(request, 'dish/order_dish.html')

# Cập nhật đơn gọi món


def update_order_status(request, order_id, status):
    try:
        OrderService.update_order_status(order_id, status)
        return redirect('view_all_tables')
    except Exception as e:
        return HttpResponseBadRequest(f"Lỗi cập nhật đơn gọi món: {str(e)}")

# Xem đơn hàng của bàn


def view_orders(request, table_id):
    orders = OrderService.get_orders_by_table(table_id)
    return render(request, 'kitchen/orders.html', {'orders': orders})
