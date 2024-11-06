from django.db import models

class Table(models.Model):
    table_id = models.AutoField(primary_key=True, db_column='TableID')
    table_number = models.IntegerField(db_column='TableNumber', null=True)
    is_available = models.BooleanField(db_column='IsAvailable', default=True)
    ability = models.IntegerField(db_column='Ability', null=True)

    class Meta:
        db_table = 'table'
