from django.db import models
from .bill_model import Bill
from .menu_model import Menu

class DishOrder(models.Model):
    dish_order_id = models.AutoField(primary_key=True, db_column='DishOrderID')
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, db_column='BillID', null=True)
    dish = models.ForeignKey(Menu, on_delete=models.CASCADE, db_column='DishID', null=True)
    number = models.IntegerField(db_column='Number', null=True)
    note = models.TextField(db_column='Note', null=True)

    class Meta:
        db_table = 'dishorder'
