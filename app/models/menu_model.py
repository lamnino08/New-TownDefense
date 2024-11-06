from django.db import models
from .categorydish_model import CategoryDish
from .cookmethod_model import CookMethod

class Menu(models.Model):
    dish_id = models.AutoField(primary_key=True, db_column='DishID')
    name = models.TextField(db_column='Name', null=True)
    category = models.ForeignKey(CategoryDish, on_delete=models.SET_NULL, db_column='CategoryID', null=True)
    cook_method = models.ForeignKey(CookMethod, on_delete=models.SET_NULL, db_column='CookMethodID', null=True)
    description = models.TextField(db_column='Description', null=True)
    picture = models.TextField(db_column='Picture', null=True)
    price = models.FloatField(db_column='Price', null=True)
    is_available = models.BooleanField(db_column='IsAvailable', default=True)

    class Meta:
        db_table = 'menu'
