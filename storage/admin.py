from django.contrib import admin
from .models import Categories, Products


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price', 'in_stock', 'is_active', 'created_on', 'updated_on']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}