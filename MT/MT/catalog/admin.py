from django.contrib import admin
from .models import Product

admin.site.register(Product)

# Register your models here.
from .models import Product, Category

admin.site.register(Category)
