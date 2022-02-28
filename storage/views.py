from django.shortcuts import render
from .models import Categories, Products

def products_list(request):
    products = Products.objects.filter(is_active=True)
    return render(request, 'storage/home.html', {'products': products})