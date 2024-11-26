from traceback import format_tb
from django.utils.html import format_html
from django.contrib import admin
from myapp.models import Bill, BillDish, Contact, Category, Table, Team, Dish, Profile, Order
from django.http import HttpResponseRedirect
from .forms import BillForm
from django.urls import path
from django.shortcuts import render, get_object_or_404

admin.site.site_header = "FiveFood | admin"


def view_dishes_in_table(modeladmin, request, queryset):
    for table in queryset:
        if table.is_occupied and table.current_bill:
            # Chuyển hướng đến hóa đơn chi tiết của bàn
            return HttpResponseRedirect(f"/admin/myapp/bill/{table.current_bill.id}/change/")
        else:
            modeladmin.message_user(
                request, f"Bàn {table.name} hiện không có khách.")


view_dishes_in_table.short_description = "Xem món trong bàn"


class TableAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_occupied', 'current_bill_display']
    list_filter = ['is_occupied']
    search_fields = ['name']
    actions = ['create_new_bill']

    def current_bill_display(self, obj):
        if obj.current_bill:
            return format_html(
                '<a href="/admin/myapp/bill/{}/change/">Hóa đơn #{}</a>',
                obj.current_bill.id,
                obj.current_bill.id
            )
        return format_html(
            '<a href="/admin/myapp/bill/add/?table={}">Tạo hóa đơn mới</a>',
            obj.id
        )
    current_bill_display.short_description = "Hóa đơn hiện tại"

    def create_new_bill(self, request, queryset):
        for table in queryset:
            if not table.current_bill:
                Bill.objects.create(table=table, total_price=0, is_payed=False)
        self.message_user(
            request, f"{queryset.count()} hóa đơn mới đã được tạo.")
    create_new_bill.short_description = "Tạo hóa đơn mới"


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email',
                    'subject', 'added_on', 'is_approved']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'added_on', 'updated_on']


class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'added_on', 'updated_on']


class DishAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'added_on', 'updated_on']
    # actions = [mark_as_paid_and_redirect]


class BillDishInline(admin.TabularInline):
    model = BillDish
    extra = 1  # Số dòng mặc định để thêm món ăn.


class BillAdmin(admin.ModelAdmin):
    list_display = ['id', 'table', 'total_price', 'is_payed', 'time']
    list_filter = ['is_payed', 'time']
    search_fields = ['table__name', 'customer__user__username']
    inlines = [BillDishInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.is_payed:
            obj.table.is_occupied = False
        else:
            obj.table.is_occupied = True
        obj.table.save()


admin.site.register(Table, TableAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(Profile)
admin.site.register(Order)
