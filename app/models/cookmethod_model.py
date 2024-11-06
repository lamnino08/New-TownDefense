from django.db import models

class CookMethod(models.Model):
    cook_method_id = models.AutoField(primary_key=True, db_column='CookMethodID')
    name = models.TextField(db_column='Name', null=True)
    description = models.TextField(db_column='Description', null=True)

    class Meta:
        db_table = 'cookmethod'
