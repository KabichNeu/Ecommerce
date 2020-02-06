from django.urls import path
from cart.views import cart_add,cart_remove,cart_detail
from products.models import Product

app_name = "cart"

urlpatterns = [
    path('',cart_detail,name = 'cart_detail'),
    path('add/(?P<product_id>\d+)',cart_add,name='cart_add'),
    path('remove/(?P<product_id>\d+)',cart_remove,name='cart_remove'),

]