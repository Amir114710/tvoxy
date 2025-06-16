from django.shortcuts import get_object_or_404, render
from django.views.generic import *

from blog.models import Tag
from .models import Category, Product

class ShopView(ListView):
    template_name = 'shop/shop.html'
    context_object_name = 'products'
    paginate_by = 8
    model = Product
    def get_queryset(self):
          return Product.objects.filter(status=True)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

class ProductDetailView(DetailView):
    template_name = 'shop/product_detail.html'
    model = Product
    context_object_name = 'product'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()[:5]
        context['products_related'] = Product.objects.all()[:4]
        context['categories'] = Category.objects.all()
        return context
    
class CategoryProductView(View):
    template_name = 'shop/shop.html'
    def get(self , request , pk):
        category = get_object_or_404(Category , id=pk)
        categories = Category.objects.all()
        products = category.products.all()
        return render(request , self.template_name , {'products':products , 'category':categories})
    
class SearchBox(TemplateView):
    queryset = None
    template_name = "shop/shop.html"
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')
        queryset =  Product.objects.filter(title__icontains = q)
        return render(request, self.template_name, {'products': queryset})