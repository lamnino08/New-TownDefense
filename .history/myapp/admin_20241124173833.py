from django.utils.html import format_html
from django.contrib import admin
from myapp.models import Bill, BillDish, Table, Dish, Order


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_occupied', 'current_bill_display']

    def current_bill_display(self, obj):
        current_bill = obj.get_current_unpaid_bill()
        if current_bill:
            return format_html(
                '<a href="/admin/myapp/bill/{}/change/">Bill #{}</a> - {}',
                current_bill.id, current_bill.id, current_bill.time.strftime(
                    '%Y-%m-%d %H:%M:%S')
            )
        return "No unpaid bills"
    current_bill_display.short_description = "Hóa đơn chưa thanh toán"


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['id', 'table', 'total_price', 'is_payed', 'time']
    list_filter = ['is_payed', 'time']


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_available', 'added_on']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['item', 'status', 'ordered_on']
    list_filter = ['status']
