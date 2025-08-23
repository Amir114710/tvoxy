from django.shortcuts import render , get_object_or_404 , redirect
from django.views.generic import View , DetailView , ListView , TemplateView
from .models import *
from mixins import *
from .extention import send_verification_email

class RepairView(ListView):
    template_name = 'repair/repair_list.html'
    model = Repair
    context_object_name = 'repair'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context
    
class RepairDetailView(DetailView):
    template_name = 'repair/repair_detail.html'
    model = Repair
    context_object_name = 'repair'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = CategoryMobile.objects.all()
        return context

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
   
class CategoryProductView(View):
    template_name = 'repair/repair_list.html'
    def get(self , request , pk):
        category = get_object_or_404(Category , pk=pk)
        product = category.repair_category.all()
        categories = Category.objects.all()
        return render(request , self.template_name , {'repair':product , 'category':categories})
    
class CategoryMobileProductView(View):
    template_name = 'repair/repair_detail_category.html'
    def get(self , request , pk):
        category = get_object_or_404(CategoryMobile , pk=pk)
        product = category.mobile_repair_category.all()
        categories = CategoryMobile.objects.all()
        return render(request , self.template_name , {'repair':product , 'category':categories})
   
class SearchBox(TemplateView):
    queryset = None
    template_name = "repair/repair_list.html"
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')
        queryset =  Repair.objects.filter(title__icontains = q)
        return render(request, self.template_name, {'repair': queryset})
    
class RepairInfo(View):
    template_name = 'repair/repair2_detail.html'
    def get(self , request):
        repair_info = RepairInfoModel.objects.all()[:1]
        brands = Brand.objects.all()[:5]
        attr = RepairAttributes.objects.all()[:3]
        return render(request , self.template_name , {'brands':brands , 'repair_info':repair_info , 'attr':attr})

class RepairReservation(LogoutRequirdMixins ,View):
    template_name = 'repair/reserve_repair.html'
    def get(self , request):
        repair_kinds = RepairKind.objects.all()
        dates = DateTimeModel.objects.all()
        return render(request , self.template_name , {'repair_kinds':repair_kinds , 'dates':dates})
    def post(self , request):
        user = request.user
        dates = request.POST.get('dates')
        repair_kinds = request.POST.get('repair_kinds')
        model_phone = request.POST.get('model_phone')
        Full_name = request.POST.get('Full_name')
        phone_number = request.POST.get('phone_number')
        description = request.POST.get('description')
        Reservation.objects.create(user=user , day_time=dates , repair_kind=repair_kinds , model_phone=model_phone , Full_name=Full_name , phone_number=phone_number , description=description)
        send_verification_email()
        return render(request , 'repair/reserve_sucess.html' , {})
        