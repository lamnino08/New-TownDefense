from myapp.models import Table, Dish, Category
import random

# Thêm 50 bàn với sức chứa từ 4-10 người
for i in range(1, 51):  # Tạo bàn từ 1 đến 50
    table_name = f"Table {i}"
    capacity = random.randint(4, 10)  # Sức chứa từ 4 đến 10 người
    Table.objects.create(name=table_name, is_occupied=False)

print("50 bàn đã được thêm vào cơ sở dữ liệu.")

# Thêm danh mục món ăn (nếu cần)
categories = [
    "Starter", "Main Course", "Dessert", "Drinks", "Seafood", "Vegetarian",
    "Fast Food", "Grilled", "Soup", "Salad"
]

for category_name in categories:
    Category.objects.get_or_create(
        name=category_name, description=f"Category for {category_name}")

print("Danh mục món ăn đã được thêm.")

# Thêm các món ăn (tổng cộng để có 20 món ăn)
dishes = [
    {"name": "Grilled Chicken", "ingredients": "Chicken, Spices",
        "price": 100000, "discounted_price": 90000, "category": "Grilled"},
    {"name": "Vegetable Salad", "ingredients": "Lettuce, Tomato, Cucumber",
        "price": 50000, "discounted_price": 45000, "category": "Salad"},
    {"name": "Tomato Soup", "ingredients": "Tomato, Spices, Cream",
        "price": 60000, "discounted_price": 55000, "category": "Soup"},
    {"name": "Fried Rice", "ingredients": "Rice, Egg, Vegetables",
        "price": 80000, "discounted_price": 75000, "category": "Main Course"},
    {"name": "Chocolate Cake", "ingredients": "Chocolate, Flour, Sugar",
        "price": 120000, "discounted_price": 110000, "category": "Dessert"},
    {"name": "Fish Curry", "ingredients": "Fish, Curry, Spices",
        "price": 150000, "discounted_price": 140000, "category": "Seafood"},
    {"name": "Ice Cream", "ingredients": "Milk, Sugar, Flavoring",
        "price": 40000, "discounted_price": 35000, "category": "Dessert"},
    {"name": "Fruit Juice", "ingredients": "Mixed Fruits",
        "price": 30000, "discounted_price": 25000, "category": "Drinks"},
    {"name": "Beef Burger", "ingredients": "Beef, Bread, Lettuce",
        "price": 120000, "discounted_price": 110000, "category": "Fast Food"},
    {"name": "Chicken Pizza", "ingredients": "Chicken, Cheese, Bread",
        "price": 150000, "discounted_price": 140000, "category": "Fast Food"},
    {"name": "Seafood Platter", "ingredients": "Shrimp, Fish, Crab",
        "price": 200000, "discounted_price": 190000, "category": "Seafood"},
    {"name": "Grilled Vegetables", "ingredients": "Zucchini, Bell Pepper, Olive Oil",
        "price": 70000, "discounted_price": 65000, "category": "Vegetarian"},
    {"name": "Pasta Alfredo", "ingredients": "Pasta, Cream, Parmesan",
        "price": 130000, "discounted_price": 120000, "category": "Main Course"},
    {"name": "Spaghetti Bolognese", "ingredients": "Spaghetti, Beef, Tomato Sauce",
        "price": 140000, "discounted_price": 130000, "category": "Main Course"},
    {"name": "Caesar Salad", "ingredients": "Romaine, Croutons, Caesar Dressing",
        "price": 90000, "discounted_price": 85000, "category": "Salad"},
    {"name": "Shrimp Cocktail", "ingredients": "Shrimp, Sauce, Lettuce",
        "price": 100000, "discounted_price": 95000, "category": "Seafood"},
    {"name": "Lemonade", "ingredients": "Lemon, Sugar, Water",
        "price": 20000, "discounted_price": 15000, "category": "Drinks"},
    {"name": "French Fries", "ingredients": "Potato, Salt, Oil",
        "price": 40000, "discounted_price": 35000, "category": "Fast Food"},
    {"name": "Cheese Sandwich", "ingredients": "Bread, Cheese, Butter",
        "price": 50000, "discounted_price": 45000, "category": "Starter"},
    {"name": "Roast Chicken", "ingredients": "Chicken, Herbs, Butter",
        "price": 170000, "discounted_price": 160000, "category": "Grilled"}
]

for dish in dishes:
    category = Category.objects.get(name=dish["category"])
    Dish.objects.create(
        name=dish["name"],
        ingredients=dish["ingredients"],
        price=dish["price"],
        discounted_price=dish["discounted_price"],
        category=category
    )

print("20 món ăn đã được thêm vào cơ sở dữ liệu.")
