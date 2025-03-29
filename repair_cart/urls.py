from django.urls import path
from .views import *

app_name = 'repair_cart_app'

urlpatterns = [
    path('' , CartDetailView.as_view() , name='cart_main'),
    path('add/<int:id>' , CartAddView.as_view() , name='cart_add'),
    path('delete/<str:id>' , CartDeleteView.as_view() , name='cart_delete'),
    path('order_detail/<int:pk>' , OrderDetailView.as_view() , name='order_detail'),
    path('order_add' , OrderCreationView.as_view() , name='order_add'),
    path('apply_discount/<int:pk>' , ApplyDiscountView.as_view() , name='apply_discount'),
    path('apply_address/<int:pk>' , ApplyAddress.as_view() , name='apply_address'),
]