from django.shortcuts import render , redirect , get_object_or_404
from django.urls import reverse
from django.views.generic import View , DeleteView
from .models import *
from home.models import *

class ServiceAttrView(View):
    template_name = 'service/service.html'
    def get(self , request):
        service_attrs = ServiceAttr.objects.all()
        moreattrs = MoreAttributes.objects.all()
        return render(request , self.template_name , {'service_attrs':service_attrs , 'moreattrs':moreattrs})
    
class TicketListView(View):
    template_name = 'service/service_ticket.html'
    def get(self , request):
        tickets = Ticket.objects.filter(user=request.user)
        return render(request , self.template_name , {'tickets':tickets})
    
class CreateTicket(View):
    template_name = 'service/ticket_create.html'
    def get(self , request):
        return render(request , self.template_name , {})
    def post(self , request):
        user = request.user
        subject = request.POST.get('subject')
        phone_brand = request.POST.get('phone_brand')
        phone_model = request.POST.get('phone_model')
        discrip = request.POST.get('discrip')
        ticket = Ticket.objects.create(user = user , subject = subject , phone_brand = phone_brand , phone_model = phone_model , discription = discrip)
        return redirect(f'http://127.0.0.1:8000/service/ticket_message/create/')
    
class TicketDeleteView(View):
    def get(self , request , pk):
        ticket = get_object_or_404(Ticket , id=pk)
        ticket.delete()
        return redirect(reverse('service_app:ticket_list'))

class TicketMessageCreateView(View):
    template_name = 'service/ticket_message_form.html'
    def get(self , request , id):
        ticket = get_object_or_404(Ticket , id=id)
        return render(request , self.template_name , {'ticket':ticket})
    def post(self , request , id):
        user = request.user
        ticket = get_object_or_404(Ticket , id=id)
        message = request.POST.get('message')
        TicketMessage.objects.create(user=user , ticket=ticket , message=message)
        return render(request , self.template_name , {'ticket':ticket})
