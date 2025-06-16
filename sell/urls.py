from django.urls import path
from .views import *

app_name = 'sell'

urlpatterns = [
    path('' , SellView.as_view() , name='main_sell'),
    path('sell_product/detail/<str:slug>' , SellDetailView.as_view() , name='sell_product_detail'),
    path('category/<int:pk>' , CategoryProductView.as_view() , name='category_detail'),
    path('search' , SearchBox.as_view() , name='search'),
]