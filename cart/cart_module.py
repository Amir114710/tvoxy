from shop.models import Product


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
            product = Product.objects.get(id = int(item['id']))
            item['product'] = product
            item['total'] = int(item['quantity']) * int(item['price'])
            item['unique_id'] = str(product.id)
            yield item

    def remove_cart(self):
        del self.session[CART_SESSION_ID]
        self.save()

    def add(self, product , quantity , color , storage):
        product_id = str(product.id)
        if product_id not in self.cart or color != self.cart[product_id]['color'] or storage != self.cart[product_id]['storage']:
            self.cart[product_id] = {'quantity': 0 , 'price': str(product.price) , 'color':color , 'storage':storage , 'id' : product.id}
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