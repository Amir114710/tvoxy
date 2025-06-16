from django.shortcuts import render , HttpResponse
from django.views.generic import TemplateView , ListView , View , DetailView
from .models import *

class SellView(ListView):
    template_name = 'sell/sell.html'
    model = SellProduct
    context_object_name = 'sell'
    paginate_by = 8
    def get_queryset(self):
        return SellProduct.objects.filter(status=True)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context
    
class SellDetailView(View):
    template_name = 'sell/sell_detail.html'
    def get(self , request , slug):
        sell = SellProduct.objects.get(slug=slug)
        categories = Category.objects.all()
        sell_product = SellProduct.objects.all()
        storage = Storage.objects.all()
        condition = Condition.objects.all()
        return render(request , self.template_name , {'sell':sell , 'categories':categories , 'sell_product':sell_product ,
                                                       'condition':condition , 'storage':storage})
    
class CategoryProductView(View):
    template_name = 'sell/sell.html'
    def get(self , request , pk):
        category = Category.objects.get(pk=pk)
        categories = Category.objects.all()
        sell = category.products.all()
        return render(request , self.template_name , {'sell':sell , 'category':categories})
    
class SearchBox(TemplateView):
    queryset = None
    template_name = "sell/sell.html"
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')
        queryset =  SellProduct.objects.filter(title__icontains = q)
        return render(request, self.template_name, {'sell': queryset})