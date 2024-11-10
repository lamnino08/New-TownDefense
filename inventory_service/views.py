

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse

from django.shortcuts import get_object_or_404, redirect
from .models import Ingredient
from .models import Supplier
from .forms import SupplierForm

def home_inventory(request):
    suppliers = Supplier.objects.all()
    
    return render(request, 'inventory_service/home.html', {'suppliers': suppliers})

def materials(request):
    # Lấy tất cả nguyên liệu từ bảng Ingredient
    ingredients = Ingredient.objects.all()
    return render(request, 'inventory_service/materials.html', {'ingredients': ingredients})


from django.views.decorators.http import require_POST

@require_POST
def delete_supplier(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    supplier.delete()
    return JsonResponse({'message': 'Nhà cung cấp đã được xóa thành công!'})