from django.shortcuts import render , redirect
from django.views.generic import View , TemplateView
from .models import *

class BusinessView(TemplateView):
    template_name = 'business/business.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_business'] = AboutBusiness.objects.all()[:1]
        context['attr'] = BusinessAttr.objects.all()[:6]
        return context
    
class BusinessFormView(View):
    template_name = 'business/business_form.html'
    def get(self , request):
        return render(request  , self.template_name , {})
    def post(self , request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        company_name = request.POST.get('company_name')
        company_type = request.POST.get('company_type')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        discription = request.POST.get('discription')
        Business.objects.create(first_name=first_name , last_name=last_name , company_name=company_name , company_type=company_type , email=email , phone=phone ,
                                 address=address , discription=discription)
        return render(request , 'business/business_form_succes.html' , {})