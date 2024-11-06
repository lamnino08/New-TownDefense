from django.contrib import admin
from .models.table_model import Table
from .models.bill_model import Bill
from .models.categorydish_model import CategoryDish
from .models.cookmethod_model import CookMethod
from .models.menu_model import Menu
from .models.reservation_model import Reservation
from .models.user_model import User
from .models.dishorder_model import DishOrder
from .models.staff_model import Staff
from .models.role_model import Role
from .models.department_model import Department

admin.site.register(Table)
admin.site.register(Bill)
admin.site.register(CategoryDish)
admin.site.register(CookMethod)
admin.site.register(Menu)
admin.site.register(Reservation)
admin.site.register(User)
admin.site.register(DishOrder)
admin.site.register(Staff)
admin.site.register(Role)
admin.site.register(Department)
