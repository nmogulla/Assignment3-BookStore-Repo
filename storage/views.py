from django.shortcuts import render, get_object_or_404
from .models import Categories, Products


def categories_list(request):
    return {
        'categories_list': Categories.objects.all()
    }


def products_list(request):
    products = Products.objects.filter(is_active=True)
    return render(request, 'storage/home.html', {'products': products})


def product_info(request, slug):
    item = get_object_or_404(Products, slug=slug, in_stock=True)
    return render(request, 'storage/product_detail.html', {'product': item})


def category_filter(request, category_slug):
    category = get_object_or_404(Categories, slug=category_slug)
    products = Products.objects.filter(category=category)
    return render(request, 'storage/category.html', {'category': category, 'products': products})
