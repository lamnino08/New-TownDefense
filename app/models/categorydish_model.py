from django.db import models

class CategoryDish(models.Model):
    category_id = models.AutoField(primary_key=True, db_column='CategoryID')
    name = models.TextField(db_column='Name', null=True)
    description = models.TextField(db_column='Description', null=True)

    class Meta:
        db_table = 'categorydish'
