from .models import Table, Order
from django.core.exceptions import ObjectDoesNotExist

class TableService:
    @staticmethod
    def get_all_tables():
        return Table.objects.all()

    @staticmethod
    def get_available_tables():
        return Table.objects.filter(is_available=True)

    @staticmethod
    def reserve_table(table_id):
        try:
            table = Table.objects.get(pk=table_id)
            if not table.is_available:
                raise Exception("Table is already reserved.")
            table.is_available = False
            table.save()
            return table
        except ObjectDoesNotExist:
            raise Exception("Table not found.")

    @staticmethod
    def cancel_reservation(table_id):
        try:
            table = Table.objects.get(pk=table_id)
            table.is_available = True
            table.save()
            return table
        except ObjectDoesNotExist:
            raise Exception("Table not found.")

    @staticmethod
    def update_table_status(table_id, status):
        try:
            table = Table.objects.get(pk=table_id)
            table.is_available = status
            table.save()
            return table
        except ObjectDoesNotExist:
            raise Exception("Table not found.")

class OrderService:
    @staticmethod
    def create_order(table_id, item_name, quantity, note=""):
        table = Table.objects.get(pk=table_id)
        order = Order.objects.create(table=table, item_name=item_name, quantity=quantity, note=note)
        return order

    @staticmethod
    def update_order_status(order_id, status):
        order = Order.objects.get(pk=order_id)
        order.status = status
        order.save()
        return order

    @staticmethod
    def get_orders_by_table(table_id):
        return Order.objects.filter(table__table_id=table_id)
