from django.shortcuts import render , get_object_or_404 , redirect
from django.views.generic import View , DetailView , ListView
from .models import *

class RepairView(ListView):
    template_name = 'repair/repair_list.html'
    model = Repair
    context_object_name = 'repair'
    
class RepairDetailView(DetailView):
    template_name = 'repair/repair_detail.html'
    model = Repair
    context_object_name = 'repair'

class MobileRepairDetailView(DetailView):
   template_name = 'repair/mobile_detail.html'
   model = MobileRepair
   context_object_name = 'mobile_repair'
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['repair_list'] = Repair.objects.all()[:5]
       context['categories'] = Category.objects.all()[:10]
       context['mobile_repair_list'] = MobileRepair.objects.all()[:4]
       return context
   def post(self,request,slug):
        user = request.user
        mobile_repair = get_object_or_404(MobileRepair , slug=slug)
        message = request.POST.get('message')
        Comment.objects.create(message=message , mobile_repair=mobile_repair , user=user)
        return redirect('repair_app:mobile_repair_detail' , slug)
   