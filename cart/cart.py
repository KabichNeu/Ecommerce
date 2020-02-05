from decimal import Decimal
from django.conf import settings
from products.models import Product

class Cart:
    def __init__(self,request):
        """initializing the cart"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            #saving an empty cart in session4
            cart = self.session[settings.CART_SESSION_ID]={}
        self.cart = cart
    
    def add(self,product,quantity=1,update_quantity=False):
        """Adding a product to the cart or update its quantity"""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0,'price': str(product.price)}

        if update_quantity:
            self.cart[product_id]['quantity']=quantity
        else:
            self.cart[product_id]['quantity']+=quantity
        self.save()

    def save(self):
        #updating the session cart
        self.session[settings.CART_SESSION_ID]= self.cart
        #mark the session as "modified" to make sure it is saved
        self.session.modified =True
    
    def remove(self,product):
        """Removing a product from the cart"""
        product_id =str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def __iter__(self):
        """iterating over the time in the cart and getting the products from the database"""
        product_ids = self.cart.keys()
        #GETTING THE PRODUCT OBJECTS AND ADDING THEM TO THE CART
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product
        
        for item in self.cart.values():
            item['price']=Decimal(item['price'])
            item['total_price'] = item['price']*item['quantity']
            yield item

    def __len__(self):
        """count all items in the cart"""

        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(Decimal(item['price'])*item['quantity'] for item in self.cart.values())
    
    def clear(self):
        #remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
    
