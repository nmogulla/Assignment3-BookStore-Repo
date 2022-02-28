from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=300, db_index=True)
    slug = models.SlugField(max_length=300, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(Categories, related_name='product', on_delete=models.CASCADE)
    created_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_created_user')
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=300, unique=True)
    price = models.FloatField(default=0.0)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created_on',)

    def __str__(self):
        return self.title