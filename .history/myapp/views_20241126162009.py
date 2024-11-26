from django.shortcuts import render, get_object_or_404, reverse, redirect
from myapp.models import Contact, Dish, Team, Category, Profile, Order, Table, Bill
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import paypalrestsdk
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import DishSerializer, CategorySerializer, TableSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
import json


def index(request):
    context = {}
    cats = Category.objects.all().order_by('name')
    context['categories'] = cats
    # print()
    dishes = []
    for cat in cats:
        dishes.append({
            'cat_id': cat.id,
            'cat_name': cat.name,
            'cat_img': cat.image,
            'items': list(cat.dish_set.all().values())
        })
    context['menu'] = dishes
    return render(request, 'index.html', context)


def contact_us(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get("name")
        em = request.POST.get("email")
        sub = request.POST.get("subject")
        msz = request.POST.get("message")

        obj = Contact(name=name, email=em, subject=sub, message=msz)
        obj.save()
        context['message'] = f"Dear {name}, Thanks for your time!"

    return render(request, 'contact.html', context)


def about(request):
    return render(request, 'about.html')


def team_members(request):
    context = {}
    members
