from sell.models import SellProduct


CART_SESSION_ID = 'cart'

class Cart:
    def __init__(self , request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart
    
    def __iter__(self):
        cart = self.cart.copy()
        for item in cart.values():
            sell_product = SellProduct.objects.get(id = int(item['id']))
            item['sell_product'] = sell_product
            item['total'] = int(item['quantity']) * int(item['price'])
            item['unique_id'] = str(sell_product.id)
            yield item

    def remove_cart(self):
        del self.session[CART_SESSION_ID]
        self.save()

    def add(self, sell_product , quantity , condition , storage):
        product_id = str(sell_product.id)
        if product_id not in self.cart or condition != self.cart[product_id]['condition'] or storage != self.cart[product_id]['storage']:
            self.cart[product_id] = {'quantity': 0 , 'price': str(sell_product.price) , 'condition':condition , 'storage':storage , 'id' : sell_product.id}
        self.cart[product_id]['quantity'] += int(quantity)
        self.save()

    def total(self):
        cart = self.cart.values()
        total = sum(int(item['price']) * int(item['quantity']) for item in cart)
        return total

    def delete(self , id):
        if id in self.cart:
            del self.cart[id]
            self.save()

    def save(self):
        self.session.modified = True