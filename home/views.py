from django.shortcuts import render
from django.views.generic import TemplateView , View

from blog.models import Article
from .models import *
from contactus.models import ContactUs


class HomeView(View):
    tenmplate_name = 'home/index.html'
    def get(self , request):
        posters = Poster.objects.all()[:3]
        info = CallInformation.objects.all()
        shopattr = ShopAttributes.objects.all()
        moreattr = MoreAttributes.objects.all()
        morediscrip = MoreDiscripUs.objects.all()
        contactus = ContactUs.objects.all()
        articles = Article.objects.all()[:2]
        return render(request , self.tenmplate_name , {'posters':posters , 'info':info , 'shopattr':shopattr , 'moreattr':moreattr , 'morediscrip':morediscrip , 'contactus':contactus , 'articles':articles})