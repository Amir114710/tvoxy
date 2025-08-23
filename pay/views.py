import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from cart.models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    YOUR_DOMAIN = "https://yourdomain.com"  # یا http://127.0.0.1:8000 برای تست

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=["card", "klarna", "paypal"],
        line_items=[{
            'price_data': {
                'currency': 'gbp',
                'unit_amount': order.total_price * 100,  # پوند × 100
                'product_data': {
                    'name': f"Order #{order.id}",
                },
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=YOUR_DOMAIN + f'/payment/success/?session_id={{CHECKOUT_SESSION_ID}}&order_id={order.id}',
        cancel_url=YOUR_DOMAIN + '/payment/cancel/',
    )
    return redirect(checkout_session.url)

def payment_success(request):
    session_id = request.GET.get("session_id")
    order_id = request.GET.get("order_id")
    session = stripe.checkout.Session.retrieve(session_id)

    if session.payment_status == 'paid':
        order = get_object_or_404(Order, id=order_id, user=request.user)
        order.is_pay = True
        order.save()
        return render(request, 'payment/success.html', {'order': order})
    else:
        return render(request, 'payment/error.html')


def cancel_payment(request):
    return render(request, 'payment/cancel.html')