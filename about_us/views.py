from django.shortcuts import render
from django.views import View
from .models import *
from home.models import *

class AboutUsView(View):
    template_name = 'about_us/about_us.html'
    def get(self , request):
        about_us = AboutInfo.objects.all()[:1]
        attr = ShopAttributes.objects.all()[:3]
        team = Team.objects.all()[:3]
        return render(self.request , self.template_name , {'about_us':about_us , 'attr':attr , 'team':team})