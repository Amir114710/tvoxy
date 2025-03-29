from django.shortcuts import render
from django.views.generic import *
from .models import Product

class ShopView(ListView):
    template_name = 'shop/shop.html'
    context_object_name = 'products'
    paginate_by = 8
    def get_queryset(self):
          return Product.objects.filter(status=True)