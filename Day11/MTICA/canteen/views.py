from django.shortcuts import render, get_object_or_404
from .models import Product


def menu(request):
    ob_products = Product.objects.all()
    return render(request, 'menu.html', {'products': ob_products})

def menu_detail(request, pk):
    ob_product = get_object_or_404(Product, pk=pk)
    return render(request, 'menu_detail.html', {'product': ob_product})