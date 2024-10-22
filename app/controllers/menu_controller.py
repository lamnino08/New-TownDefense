from django.shortcuts import render
from app.models.menu import Menu

def menu_list(request):
    menus = Menu.objects.all()
    return render(request, 'menu/menu_list.html', {'menus': menus})

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
