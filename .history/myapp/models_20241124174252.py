from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Table"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="categories/%Y/%m/%d")
    icon = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to="team")
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='dishes/%Y/%m/%d')
    ingredients = models.TextField()
    details = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    discounted_price = models.FloatField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def display_price(self):
        return self.discounted_price if self.discounted_price else self.price

    class Meta:
        verbose_name_plural = "Dish Table"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='profiles/%Y/%m/%d', null=True, blank=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name_plural = "Profile Table"


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    item = models.ForeignKey(Dish, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending')
    invoice_id = models.CharField(max_length=100, blank=True)
    payer_id = models.CharField(max_length=100, blank=True)
    ordered_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.user.first_name} - {self.status}"

    def update_status(self, new_status):
        self.status = new_status
        self.save()


class Table(models.Model):
    name = models.CharField(max_length=50, unique=True)
    is_occupied = models.BooleanField(default=False)
    current_bill = models.OneToOneField(
        'Bill', on_delete=models.SET_NULL, null=True, blank=True, related_name='table_bill'
    )

    def __str__(self):
        return self.name

    def get_current_unpaid_bill(self):
        return self.bills.filter(is_payed=False).order_by('-time').first()

    def mark_table_free(self):
        if not self.get_current_unpaid_bill():
            self.is_occupied = False
            self.save()

    class Meta:
        verbose_name_plural = "Danh sách bàn"


class Bill(models.Model):
    table = models.ForeignKey(
        Table, on_delete=models.SET_NULL, null=True, related_name='bills')
    customer = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    dishes = models.ManyToManyField(Dish, through='BillDish')
    total_price = models.FloatField(null=True)
    is_payed = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bill {self.id} - Table: {self.table.name}"

    def mark_as_paid(self):
        self.is_payed = True
        self.save()
        self.table.mark_table_free()

    def get_dish_details(self):
        return [
            {
                'dish_name': dish.dish.name,
                'quantity': dish.quantity,
                'total_price': dish.total_price
            } for dish in self.billdish_set.all()
        ]


class BillDish(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    note = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(default=1)

    @property
    def total_price(self):
        return self.quantity * self.dish.price

    def __str__(self):
        return f"{self.dish.name} x {self.quantity} (Bill #{self.bill.id})"
