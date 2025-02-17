from django.shortcuts import render
from django.views.generic import TemplateView , View
from .models import *


class HomeView(View):
    tenmplate_name = 'home/index.html'
    def get(self , request):
        posters = Poster.objects.all()[:3]
        info = CallInformation.objects.all()
        shopattr = ShopAttributes.objects.all()
        moreattr = MoreAttributes.objects.all()
        morediscrip = MoreDiscripUs.objects.all()
        return render(request , self.tenmplate_name , {'posters':posters , 'info':info , 'shopattr':shopattr , 'moreattr':moreattr , 'morediscrip':morediscrip})