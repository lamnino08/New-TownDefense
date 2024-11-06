from django.db import models
from .table_model import Table

class Bill(models.Model):
    bill_id = models.AutoField(primary_key=True, db_column='BillID')
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, db_column='TableID', null=True)
    is_available = models.BooleanField(db_column='IsAvailable', default=True)
    total_price = models.FloatField(db_column='TotalPrice', null=True)
    is_payed = models.BooleanField(db_column='IsPayed', default=False)
    time = models.DateTimeField(db_column='Time', null=True)

    class Meta:
        db_table = 'bill'
