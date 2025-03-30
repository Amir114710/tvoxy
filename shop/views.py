from django.shortcuts import render
from django.views.generic import *
from .models import Product

class ShopView(ListView):
    template_name = 'shop/shop.html'
    context_object_name = 'products'
    paginate_by = 8
    def get_queryset(self):
          return Product.objects.filter(status=True)

class ProductDetailView(DetailView):
    template_name = 'shop/product_detail.html'
    model = Product
    context_object_name = 'product'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()[:5]
        context['products_related'] = Product.objects.all()[:4]
        return context