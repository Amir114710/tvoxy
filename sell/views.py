from django.shortcuts import render , HttpResponse
from django.views.generic import TemplateView , ListView , View , DetailView
from .models import *
from mixins import *
from .extention import send_verification_email

class SellView(LogoutRequirdMixins , ListView):
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
    
class SellCategoryPhone(TemplateView):
    template_name = 'sell/sell_category.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sell'] = PhoneCategory.objects.all()
        return context

class CategoryPhoneView(View):
    template_name = 'sell/sell_category_form.html'
    def get(self , request , pk):
        category = PhoneCategory.objects.get(pk=pk)
        category_data = category.phone_model.all()
        condition = Condition.objects.all()
        storage = Storage.objects.all()
        return render(request , self.template_name , {'category_data':category_data ,'storage':storage , 'condition':condition})

class CategoryFormView(View):
    def post(self , request):
        phone_model = request.POST.get('phone_model')
        storage = request.POST.get('storage')
        condition = request.POST.get('condition')
        for x in PhoneModel.objects.all():
            if x.title == phone_model:
                price3 = x.price
                sell1 = x.sell_condition.all()
                sell2 = x.sell_storage.all()
        for x in sell2:
            if storage == x.storage:
                price1 = x.price
        for x in sell1:
            if condition == x.condition:
                price2 = x.price
        total_price = price1 + price2 + price3
        Sell.objects.create(user = request.user , phone=phone_model , condition=condition , storage=storage, total_price=total_price)
        send_verification_email()
        return render(self.request , 'sell/sell_sucess.html', {'total_price':total_price})
    
class SellFormView(View):
    template_name = 'sell/sell_form.html'
    def get(self , request):
        return render(request , self.template_name , {})
    def post(self , request):
        phone_number = request.POST.get('phone_number')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        account_number = request.POST.get('account_number')
        SellForm.objects.create(phone_number=phone_number , full_name=full_name , email=email , account_number=account_number)
        return render(request , 'sell/success2.html' , {})