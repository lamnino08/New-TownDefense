from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Contact, Dish, Team, Category, Profile, Order, Table
from .serializers import DishSerializer, CategorySerializer, TableSerializer

# API cho Dish (Danh sách món ăn)


class DishViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dish.objects.filter(is_available=True)
    serializer_class = DishSerializer

# API cho Category (Danh sách danh mục món ăn)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# API cho Table (Danh sách bàn và đặt bàn)


class TableViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        tables = Table.objects.all()
        serializer = TableSerializer(tables, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        user = request.user.profile  # Lấy thông tin khách hàng từ tài khoản đăng nhập
        table_id = data.get('table_id')

        try:
            table = Table.objects.get(id=table_id, is_occupied=False)
            table.is_occupied = True
            table.save()
            return Response({'message': f'Bạn đã đặt bàn {table.name} thành công.'}, status=status.HTTP_201_CREATED)
        except Table.DoesNotExist:
            return Response({'error': 'Bàn không khả dụng hoặc đã được đặt.'}, status=status.HTTP_400_BAD_REQUEST)

# Trang chủ (hiển thị menu)


def index(request):
    context = {}
    return render(request, 'index.html', context)

# Trang đặt bàn (frontend)


@login_required
def book_table(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request, 'book_table.html', {'user_profile': user_profile})

# Liên hệ


def contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        Contact.objects.create(name=name, email=email,
                               subject=subject, message=message)
        return JsonResponse({'message': f'Cảm ơn {name}, chúng tôi sẽ liên hệ lại sớm nhất!'})

    return render(request, 'contact.html')

# Đăng ký


def register(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = request.POST.get('number')
        if User.objects.filter(username=email).exists():
            context['error'] = 'Email đã tồn tại!'
        else:
            user = User.objects.create_user(
                username=email, email=email, password=password, first_name=name)
            Profile.objects.create(user=user, contact_number=contact)
            context['status'] = f'Người dùng {name} đã đăng ký thành công!'

    return render(request, 'register.html', context)

# Đăng nhập


def signin(request):
    context = {}
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/dashboard')
        else:
            context['error'] = 'Thông tin đăng nhập không chính xác!'
    return render(request, 'login.html', context)

# Dashboard


@login_required
def dashboard(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request, 'dashboard.html', {'profile': user_profile})

# Đăng xuất


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
