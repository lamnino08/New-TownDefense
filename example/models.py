from django.db import models


# Bảng Table
class Table(models.Model):
    table_id = models.AutoField(primary_key=True, db_column='TableID')
    table_number = models.IntegerField(db_column='TableNumber', null=True)
    is_available = models.BooleanField(db_column='IsAvailable', default=True)
    ability = models.IntegerField(db_column='Ability', null=True)

    class Meta:
        db_table = 'table'


# Bảng Bill
class Bill(models.Model):
    bill_id = models.AutoField(primary_key=True, db_column='BillID')
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, db_column='TableID', null=True)
    is_available = models.BooleanField(db_column='IsAvailable', default=True)
    total_price = models.FloatField(db_column='TotalPrice', null=True)
    is_payed = models.BooleanField(db_column='IsPayed', default=False)
    time = models.DateTimeField(db_column='Time', null=True)

    class Meta:
        db_table = 'bill'


# Bảng CategoryDish
class CategoryDish(models.Model):
    category_id = models.AutoField(primary_key=True, db_column='CategoryID')
    name = models.TextField(db_column='Name', null=True)
    description = models.TextField(db_column='Description', null=True)

    class Meta:
        db_table = 'categorydish'


# Bảng CookMethod
class CookMethod(models.Model):
    cook_method_id = models.AutoField(primary_key=True, db_column='CookMethodID')
    name = models.TextField(db_column='Name', null=True)
    description = models.TextField(db_column='Description', null=True)

    class Meta:
        db_table = 'cookmethod'


# Bảng Menu
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


# Bảng Reservation
class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True, db_column='ReservationID')
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, db_column='TableNumber', null=True)
    user = models.ForeignKey('User', on_delete=models.SET_NULL, db_column='UserID', null=True)
    time = models.DateTimeField(db_column='Time', null=True)
    is_taken = models.BooleanField(db_column='IsTaken', default=False)

    class Meta:
        db_table = 'reservation'


# Bảng User
class User(models.Model):
    user_id = models.AutoField(primary_key=True, db_column='UserID')
    name = models.TextField(db_column='Name', null=True)
    hash_password = models.TextField(db_column='HashPassword', null=True)
    create_at = models.DateTimeField(db_column='CreateAt', null=True)

    class Meta:
        db_table = 'user'


# Bảng DishOrder
class DishOrder(models.Model):
    dish_order_id = models.AutoField(primary_key=True, db_column='DishOrderID')
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, db_column='BillID', null=True)
    dish = models.ForeignKey(Menu, on_delete=models.CASCADE, db_column='DishID', null=True)
    number = models.IntegerField(db_column='Number', null=True)
    note = models.TextField(db_column='Note', null=True)

    class Meta:
        db_table = 'dishorder'


# Bảng Staff
class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True, db_column='StaffID')
    name = models.TextField(db_column='Name', null=True)
    phone_number = models.TextField(db_column='PhoneNumber', null=False)
    role = models.ForeignKey('Role', on_delete=models.SET_NULL, db_column='RoleID', null=True)
    password = models.TextField(db_column='Password', null=True)
    create_at = models.DateTimeField(db_column='CreateAt', null=True)
    username = models.TextField(db_column='Username', null=True)

    class Meta:
        db_table = 'staff'


# Bảng Role
class Role(models.Model):
    role_id = models.AutoField(primary_key=True, db_column='RoleID')
    name = models.TextField(db_column='Name', null=True)
    description = models.TextField(db_column='Description', null=True)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, db_column='DepartmentID', null=True)

    class Meta:
        db_table = 'role'


# Bảng Department
class Department(models.Model):
    department_id = models.AutoField(primary_key=True, db_column='DepartmentID')
    name = models.TextField(db_column='Name', null=True)
    description = models.TextField(db_column='Description', null=True)
    icon = models.TextField(db_column='Icon', null=True)

    class Meta:
        db_table = 'department'
