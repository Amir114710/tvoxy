from django.shortcuts import render
from django.views.generic import View , TemplateView
from .models import *
from home.models import *

class AboutUsView(View):
    template_name = 'about_us/about_us.html'
    def get(self , request):
        about_us = AboutInfo.objects.all()[:1]
        attr = ShopAttributes.objects.all()[:3]
        team = Team.objects.all()[:3]
        brand = Brand.objects.all()[:5]
        return render(self.request , self.template_name , {'about_us':about_us , 'attr':attr , 'team':team , 'brand':brand})
    
class ComeingSoon(TemplateView):
    template_name = 'about_us/comingsoon.html'