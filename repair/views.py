from django.shortcuts import render , get_object_or_404
from django.views.generic import View
from .models import *

class RepairView(View):
    template_name = 'repair/repair_list.html'
    def get(self , request):
        repair = Repair.objects.all()
        return render(request , self.template_name , {'repair':repair})
    
class RepairDetailView(View):
    template_name = 'repair/repair_detail.html'
    def get(self , request , id):
        repair = get_object_or_404(Repair , id=id)
        return render(request , self.template_name , {'repair':repair})

class MobileRepairDetailView(View):
    template_name = 'repair/mobile_detail.html'
    def get(self , request , id):
        mobile_repair = get_object_or_404(MobileRepair , id=id)
        return render(request , self.template_name , {'mobile_repair':mobile_repair})