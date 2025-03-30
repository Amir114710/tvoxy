from django.shortcuts import render , redirect , reverse
from django.views.generic import FormView , TemplateView , CreateView , View
from uuid import uuid4
from mixins import LoginRequirdMixins , LogoutRequirdMixins , AddressRequirdMixins
from django.urls import reverse_lazy
from django.contrib.auth import login , authenticate , logout
import requests
from .form import RegisterForm , OtpForm , Edite_Profile_Form , AddressCreationForm
from random import randint
from .models import OTP, User
from .extention import *

class OtpRegisterationView(LoginRequirdMixins , FormView):
    template_name = 'account/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home:main')
    def form_valid(self, form):
        email = self.request.POST.get('email')
        random_code = randint(1000 , 9999)
        token = str(uuid4())
        OTP.objects.create(email = email , code = random_code , token = token)
        send_verification_email(email , random_code)
        print(random_code)
        return redirect(reverse('account:check_otp') + f'?token={token}')

class CheckOtpCode(LoginRequirdMixins , FormView):
    template_name = 'account/otp_form.html'
    form_class = OtpForm
    success_url = reverse_lazy('home_app:home')
    def form_valid(self, form):
        token = self.request.GET.get('token')
        code = self.request.POST.get('code')
        if OTP.objects.filter(code=code , token=token).exists():
            otp = OTP.objects.get(token=token)
            user , is_created = User.objects.get_or_create(email = otp.email)
            login(self.request , user)
            otp.delete()
            return redirect('account:edit_profile')       
        else:
            form.add_error(code , 'this information is not correct')
        return render(self.request , self.template_name , {'form':form})

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect(reverse('home:main'))
    else:
        return redirect(reverse('home:main'))


class ProfileView(LogoutRequirdMixins , TemplateView) :
    template_name = 'account/profile.html'


def profile_edite(request):
    if request.user.is_authenticated == True:
        user = request.user
        form = Edite_Profile_Form(instance=user)
        if request.method == 'POST':
            form = Edite_Profile_Form(request.POST  , request.FILES ,instance=user)
            if form.is_valid():
                form.save()
                return redirect('account:profile')
        else:
            form = Edite_Profile_Form(instance=user)
        return render(request , 'account/edite_profile.html' , {'form':form})
    else:
        return redirect('home:main')
    
class AddAdressView(AddressRequirdMixins , View):
    def post(self , request):
        form = AddressCreationForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)
            return render(request , 'account/address.html' , {'form':form})
        return render(request , 'account/address.html' , {'form':form})

    def get(self , request):
        form = AddressCreationForm()
        return render(request , 'account/address.html' , {'form':form})
         
