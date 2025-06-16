from django.shortcuts import render , redirect , get_object_or_404
from django.views.generic import View , TemplateView
from django.urls import reverse
from account.models import Address
from repair_cart.cart_module import Cart
from repair.models import MobileRepair
from .cart_module import Cart
from .models import DiscountCode, Order, OrderItem

class CartDetailView(TemplateView):
    template_name = 'repair_cart/repair_cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context

class CartAddView(View):
    template_name = 'repair_cart/repair_cart.html'
    def post(self , request , id):
        mobile_reapir = get_object_or_404(MobileRepair , id = id)
        quantity = request.POST.get('quantity')
        cart = Cart(request)
        if int(quantity) > 0:
            cart.add(mobile_reapir , quantity)
        cart = Cart(self.request)
        return redirect('repair_cart_app:cart_main')
    
class CartDeleteView(View):
    def get(self , request , id):
        cart = Cart(request)
        cart.delete(id)
        return redirect(reverse('repair_cart_app:cart_main'))
    
class OrderDetailView(View):
    def get(self , request , pk):
        order = get_object_or_404(Order , id=pk)
        return render(request , 'repair_cart/checkout.html' , {'order':order})

class OrderCreationView(View):
    def get(self , request):
        cart = Cart(request)
        order = Order.objects.create(user = request.user , total_price = cart.total())
        for item in cart:
            OrderItem.objects.create(order=order , mobile_repair = item['mobile_repair'] , quantity = item['quantity'] , price = item['price'])

        cart.remove_cart()
        return redirect('repair_cart_app:order_detail' , order.id)

class ApplyDiscountView(View):
    def post(self , request , pk):
        code = request.POST.get('discount_code')
        order = get_object_or_404(Order , id=pk)
        discount_code = get_object_or_404(DiscountCode , name=code)
        if discount_code.quantity == 0 :
            return redirect('cart:order_detail' , order.id)
        order.total_price -= order.total_price * discount_code.discount/100
        order.save()
        discount_code.quantity -= 1
        discount_code.save()
        return redirect('repair_cart_app:order_detail' , order.id)

class ApplyAddress(View):
    def post(self , request , pk):
        order = get_object_or_404(Order , id=pk)
        address = request.POST.get('address')
        order.addresses = address
        order.save()
        return redirect('pay:main_pay' , order.id)