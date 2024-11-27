from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DishViewSet, CategoryViewSet, TableViewSet

# Tạo router cho API
router = DefaultRouter()
router.register(r'dishes', DishViewSet, basename='dishes')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'tables', TableViewSet, basename='tables')

urlpatterns = [
    # Các URL cũ
    path('', include('django.contrib.auth.urls')),
    path('book_table/', include(router.urls)),  # Đặt bàn API
]
