

from django.http import HttpResponse
from django.shortcuts import redirect, render
from store.models import Product

def index(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products': products
    }
    return render(request, 'ecommerce/index.html', context)

