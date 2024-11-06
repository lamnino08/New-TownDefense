from django.db import models
from .table_model import Table
from .user_model import User

class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True, db_column='ReservationID')
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, db_column='TableNumber', null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, db_column='UserID', null=True)
    time = models.DateTimeField(db_column='Time', null=True)
    is_taken = models.BooleanField(db_column='IsTaken', default=False)

    class Meta:
        db_table = 'reservation'
