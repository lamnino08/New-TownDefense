# restaurant_management/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth_service.urls')),
    path('table/', include('table_service.urls')),
    path('', include('auth_service.urls')),
]