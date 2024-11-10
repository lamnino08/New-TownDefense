from django.db import models

class Ingredient(models.Model):
    ingredient_code = models.CharField(max_length=100)  # Mã nguyên liệu
    ingredient_name = models.CharField(max_length=255)  # Tên nguyên liệu
    stock_quantity = models.IntegerField()  # Số lượng tồn kho
    unit = models.CharField(max_length=50)  # Đơn vị tính
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)  # Đơn giá
    stock_value = models.DecimalField(max_digits=10, decimal_places=2)  # Giá trị tồn kho
    import_date = models.DateField()  # Ngày nhập kho
    expiry_date = models.DateField()  # Ngày hết hạn
    supplier_name = models.CharField(max_length=255)  # Tên nhà cung cấp
    status = models.CharField(max_length=100)  # Trạng thái nguyên liệu

    class Meta:
        db_table = 'inventory_service_ingredient'  # Chỉ định tên bảng trong cơ sở dữ liệu

    def __str__(self):
        return self.ingredient_name


class Supplier(models.Model):
    supplier_code = models.CharField(max_length=20, unique=True)  # Mã nhà cung cấp
    name = models.CharField(max_length=255)  # Tên nhà cung cấp
    address = models.CharField(max_length=255)  # Địa chỉ
    phone = models.CharField(max_length=15)  # Điện thoại
    email = models.EmailField()  # Email

    class Meta:
        db_table = 'supplier'  # Chỉ định tên bảng trong cơ sở dữ liệu

    def __str__(self):
        return self.name  # Trả về tên nhà cung cấp khi gọi đến đối tượng Supplier
