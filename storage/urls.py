from django.urls import path
from . import views

app_name = 'storage'

urlpatterns = [
    path('', views.products_list, name='products_list'),
    path('<slug:slug>', views.product_info, name='product_info'),
    path('search/<slug:category_slug>/', views.category_filter, name='category_filter')
]
