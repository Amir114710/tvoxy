from django.urls import path
from .views import *

app_name = 'sell'

urlpatterns = [
    path('' , SellView.as_view() , name='main_sell'),
    path('sell_product/detail/<str:slug>' , SellDetailView.as_view() , name='sell_product_detail'),
    path('category/<int:pk>' , CategoryProductView.as_view() , name='category_detail'),
    path('search' , SearchBox.as_view() , name='search'),
    path('phone_category' , SellCategoryPhone.as_view() , name='phone_category'),
    path('category/phone/model/detail/<int:pk>' , SellModelPhone.as_view() , name='category_phone_model'),
    path('category/phone/detail/<int:pk>' , CategoryPhoneView.as_view() , name='category_phone_detail'),
    path('category/phone/detail/form' , CategoryFormView.as_view() , name='category_form_view'),
    path('sell/form' , SellFormView.as_view() , name='sell_form'),
]