from django.shortcuts import render
from django.views.generic import TemplateView , View
from .models import *

class CharityView(TemplateView):
    template_name = 'charity/charity.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_charity'] = AboutCharity.objects.all()[:1]
        context['attr'] = CharityAttr.objects.all()[:1]
        return context

class CharityFormView(View):
    template_name = 'charity/charity_form.html'
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
        Charity.objects.create(first_name=first_name , last_name=last_name , company_name=company_name , company_type=company_type , email=email , phone=phone ,
                                 address=address , discription=discription)
        return render(request , 'charity/charity_form_succes.html' , {})