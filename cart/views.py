from django.shortcuts import render , redirect , get_object_or_404
from django.views.generic import View , TemplateView
from django.urls import reverse
from account.models import Address
from cart.cart_module import Cart
from shop.models import Product
from .cart_module import Cart
from .models import DiscountCode, Order, OrderItem
from mixins import AddressRequirdMixins, LoginRequirdMixins , LogoutRequirdMixins

class CartDetailView(TemplateView):
    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context

class CartAddView(View):
    def post(self , request , slug):
        product = get_object_or_404(Product , slug = slug)
        quantity = request.POST.get('quantity')
        color = request.POST.get('color')
        storage = request.POST.get('storage')
        for x in product.product_storage.all():
            if storage == x.storage:
                storage_price = x.price
        for x in product.product_color.all():
            if color == x.color:
                color_price = x.price
        product_price = storage_price + color_price
        product.price = product_price
        product.save()
        cart = Cart(request)
        print(quantity)
        if int(quantity) > 0:
            cart.add(product , quantity , color , storage)
        return redirect(reverse('cart:cart_main'))
    
class CartDeleteView(View):
    def get(self , request , id):
        cart = Cart(request)
        cart.delete(id)
        return redirect(reverse('shop:shop_main'))
    
class OrderDetailView(View):
    def get(self , request , pk):
        order = get_object_or_404(Order , id=pk)
        return render(request , 'cart/checkout.html' , {'order':order})

class OrderCreationView(View):
    def get(self , request):
        cart = Cart(request)
        order = Order.objects.create(user = request.user , total_price = cart.total())
        for item in cart:
            OrderItem.objects.create(order=order , product = item['product'] , quantity = item['quantity'] , color = item['color'] ,
                                      storage = item['storage'] , price = item['price'])
        cart.remove_cart()
        return redirect('cart:order_detail' , order.id)
    
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
        return redirect('cart:order_detail' , order.id)

class ApplyAddress(View):
    def post(self , request , pk):
        order = get_object_or_404(Order , id=pk)
        address = request.POST.get('address')
        order.addresses = address
        order.save()
        return redirect('pay:main_pay' , order.id)