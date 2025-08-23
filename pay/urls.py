from django.urls import path
from . import views

app_name = 'pay'

urlpatterns = [
    path('payment/checkout/<int:order_id>/', views.create_checkout_session, name='create_payment'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('payment/cancel/', views.cancel_payment, name=''),
]