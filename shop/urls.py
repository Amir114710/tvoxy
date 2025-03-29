from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('' , ShopView.as_view() , name='shop_main'),
]