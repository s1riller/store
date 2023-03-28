from django.shortcuts import render
from products.models import Product, ProductCategory
# Create your views here.

# Функция = контроллер = въюха = обработчик запроса

def index(request):
    context = {'title': 'Store',
               }
    return render(request, 'products/index.html', context)


def products(request):
    context = {'title': 'Store - Каталог',
               'products': Product.objects.all(),
               'categories': ProductCategory.objects.all()}
    return render(request, 'products/products.html', context)
