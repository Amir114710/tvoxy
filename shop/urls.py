from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('' , ShopView.as_view() , name='shop_main'),
    path('product_detail/<str:slug>' , ProductDetailView.as_view() , name='product_detail')
]