from django.urls import path
from .views import *

app_name = 'sell_pay'

urlpatterns = [
    path('after_pay' , AfterPayView.as_view() , name='after_pay'),
    path('payment/checkout/<int:order_id>/', create_checkout_session, name='create_payment'),
    path('payment/success/', payment_success, name='payment_success'),
    path('payment/cancel/', cancel_payment, name='payment_cancel'),
]