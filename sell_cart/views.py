from django.shortcuts import render , redirect , get_object_or_404
from django.views.generic import View , TemplateView
from django.urls import reverse
from account.models import Address
from sell_cart.cart_module import Cart
from sell.models import SellProduct
from .cart_module import Cart
from .models import DiscountCode, Order, OrderItem
from mixins import AddressRequirdMixins, LoginRequirdMixins , LogoutRequirdMixins

class CartDetailView(TemplateView):
    template_name = 'sell_cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context

class CartAddView(View):
    def post(self , request , slug):
        sell_product = get_object_or_404(SellProduct , slug = slug)
        quantity = request.POST.get('quantity')
        condition = request.POST.get('condition')
        storage = request.POST.get('storage')
        for x in sell_product.sell_storage.all():
            if storage == x.storage:
                storage_price = x.price
        for x in sell_product.sell_condition.all():
            if condition == x.condition:
                condition_price = x.price
        sell_product_price = storage_price + condition_price
        print(sell_product_price)
        sell_product.price = sell_product_price
        sell_product.save()
        print(sell_product.price)
        cart = Cart(request)
        if int(quantity) > 0:
            cart.add(sell_product , quantity , condition , storage)
        return redirect(reverse('sell_cart:cart_main'))
    
class CartDeleteView(View):
    def get(self , request , id):
        cart = Cart(request)
        cart.delete(id)
        return redirect(reverse('sell:main_sell'))
    
class OrderDetailView(View):
    def get(self , request , pk):
        order = get_object_or_404(Order , id=pk)
        return render(request , 'sell_cart/checkout.html' , {'order':order})

class OrderCreationView(View):
    def get(self , request):
        cart = Cart(request)
        order = Order.objects.create(user = request.user , total_price = cart.total())
        for item in cart:
            OrderItem.objects.create(order=order , sell_product = item['sell_product'] , quantity = item['quantity'] , condition = item['condition'] ,
                                      storage = item['storage'] , price = item['price'])
        cart.remove_cart()
        return redirect('sell_cart:order_detail' , order.id)
    
class ApplyDiscountView(View):
    def post(self , request , pk):
        code = request.POST.get('discount_code')
        order = get_object_or_404(Order , id=pk)
        discount_code = get_object_or_404(DiscountCode , name=code)
        if discount_code.quantity == 0 :
            return redirect('sell_cart:order_detail' , order.id)
        order.total_price -= order.total_price * discount_code.discount/100
        order.save()
        discount_code.quantity -= 1
        discount_code.save()
        return redirect('sell_cart:order_detail' , order.id)

class ApplyAddress(View):
    def post(self , request , pk):
        order = get_object_or_404(Order , id=pk)
        address = request.POST.get('address')
        order.addresses = address
        order.save()
        return redirect('pay:main_pay' , order.id)