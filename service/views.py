from django.shortcuts import render
from django.views import View
from .models import *
from home.models import *

class ServiceAttrView(View):
    template_name = 'service/service.html'
    def get(self , request):
        service_attrs = ServiceAttr.objects.all()
        moreattrs = MoreAttributes.objects.all()
        return render(request , self.template_name , {'service_attrs':service_attrs , 'moreattrs':moreattrs})
    
class ServiceFormView(View):
    template_name = 'service/service_form.html'
    def get(self , request):
        return render(request , self.template_name , {})