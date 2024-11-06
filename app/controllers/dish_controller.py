from django.shortcuts import redirect, render
from app.models.dish_order import DishOrder
from app.models.menu import Menu

def order_dish(request):
    if request.method == 'POST':
        dish_id = request.POST.get('dish_id')
        quantity = request.POST.get('quantity')
        note = request.POST.get('note', '')
        bill_id = request.POST.get('bill_id')
        bill = Bill.objects.get(pk=bill_id)
        dish = Menu.objects.get(pk=dish_id)
        dish_order = DishOrder(bill=bill, dish=dish, number=quantity, note=note)
        dish_order.save()
        return redirect('order_dish')
    dishes = Menu.objects.filter(is_available=True)
    return render(request, 'dish/order_dish.html', {'dishes': dishes})
