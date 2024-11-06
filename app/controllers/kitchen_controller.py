from django.shortcuts import render
from app.models.dish_order import DishOrder

def kitchen_orders(request):
    dish_orders = DishOrder.objects.all()
    return render(request, 'kitchen/update_status.html', {'dish_orders': dish_orders})

def update_dish_status(request, dish_id):
    dish = Menu.objects.get(pk=dish_id)
    if request.method == 'POST':
        dish.is_available = False
        dish.save()
    return redirect('kitchen_orders')
