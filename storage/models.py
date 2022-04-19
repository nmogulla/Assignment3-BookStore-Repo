from audioop import reverse
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=300, db_index=True)
    slug = models.SlugField(max_length=300, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    # def get_absolute_url(self):
    # return reverse('storage:category_list', args=[self.slug])

    def get_absolute_url(self):
        return reverse('storage:category_filter', args=[self.slug])

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(Categories, related_name='product', on_delete=models.CASCADE)
    created_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                     related_name='product_created_user')
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
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

    def get_absolute_url(self):
        return reverse('storage:product_info', args=[self.slug])
