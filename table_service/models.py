from django.db import models


class Table(models.Model):
    table_id = models.AutoField(primary_key=True, db_column='TableID')
    table_number = models.IntegerField(unique=True, db_column='TableNumber')
    is_available = models.BooleanField(default=True, db_column='IsAvailable')
    capacity = models.IntegerField(db_column='Ability')

    class Meta: db_table = 'table'

    def __str__(self): return f"Table {self.table_number}"


class Order(models.Model):
    reservation_id = models.AutoField(primary_key=True, db_column='ReservationID')
    table_number = models.IntegerField(db_column='TableNumber')
    user_id = models.IntegerField(db_column='UserID')
    time = models.DateTimeField(db_column='Time')
    is_taken = models.BooleanField(default=False, db_column='IsTaken')

    class Meta: db_table = 'reservation'

    def __str__(self): return f"Reservation {self.reservation_id} for Table {self.table_number}"
