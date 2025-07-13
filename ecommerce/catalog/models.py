from django.db import models
from django.contrib.auth.models import User
from your_app_name.models import Category


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products',null=True, blank=True)

    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
