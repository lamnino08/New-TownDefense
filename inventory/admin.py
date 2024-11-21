from django.contrib import admin
from .models import *
from django.utils.html import format_html
from .models import PurchaseOrder, PurchaseOrderDetail, Ingredient
from .forms import PurchaseOrderForm, PurchaseOrderDetailForm
from decimal import Decimal


class IngredientAdmin (admin.ModelAdmin):
    list_display = ('code', 'name', 'unit', 'price', 'quantity', 'added_on')  # Các trường sẽ hiển thị trong danh sách
    search_fields = ('code', 'name')
    list_filter = ('unit', 'added_on')  # Bộ lọc theo đơn vị và ngày thêm
    ordering = ('code',)  # Sắp xếp theo mã nguyên liệu

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name','phone_number', 'email', 'address', 'added_on')  # Hiển thị các trường mong muốn
    search_fields = ('name', 'contact_number', 'email')  # Tìm kiếm theo tên, số liên lạc và email
    list_filter = ('added_on',)  # Bộ lọc theo ngày thêm nhà cung ứng
    ordering = ('name',)  # Sắp xếp theo tên nhà cung ứng


    
class StockOutAdmin(admin.ModelAdmin):
    list_display = ['id', 'ingredient', 'quantity', 'unit', 'date_out']  # Hiển thị các trường mong muốn
    list_filter = ['date_out', 'ingredient']  # Bộ lọc theo ngày xuất và nguyên liệu
    search_fields = ['ingredient__name', 'unit']  # Tìm kiếm theo tên nguyên liệu và đơn vị


class PurchaseOrderDetailInline(admin.TabularInline):
    model = PurchaseOrderDetail
    form = PurchaseOrderDetailForm
    extra = 1  # Dòng trống mặc định cho việc thêm nguyên liệu
    fields = ['ingredient', 'quantity', ]
    

class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['order_code', 'order_date', 'is_received', 'time']
    form = PurchaseOrderForm
    inlines = [PurchaseOrderDetailInline]
    search_fields = ['order_code']
    list_filter = ['is_received', 'order_date']

admin.site.register(PurchaseOrder, PurchaseOrderAdmin)



admin.site.register(StockOut, StockOutAdmin)

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Supplier, SupplierAdmin)
