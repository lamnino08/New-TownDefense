from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True, db_column='UserID')
    name = models.TextField(db_column='Name', null=True)
    hash_password = models.TextField(db_column='HashPassword', null=True)
    create_at = models.DateTimeField(db_column='CreateAt', null=True)

    class Meta:
        db_table = 'user'
