from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from home.models import CallInformation
from .models import ContactUs


class ContactUsView(View):
    template_name = 'contactus/contactus.html'
    def get(self , request):
        callinformation = CallInformation.objects.all()[:1]
        return render(request , self.template_name , {'callinformation':callinformation})
    def post(self , request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactUs.objects.create(name = name , email = email , message = message)
        return redirect(reverse('home:main'))