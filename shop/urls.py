from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('' , ShopView.as_view() , name='shop_main'),
    path('product_detail/<str:slug>' , ProductDetailView.as_view() , name='product_detail'),
    path('category-product/<int:pk>' , CategoryProductView.as_view() , name='category-product'),
    path('search' , SearchBox.as_view() , name='search'),
]