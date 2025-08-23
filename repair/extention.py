from django.core.mail import send_mail
from django.conf import settings

def send_verification_email():
    subject = 'reservation'
    message = f'reservation'
    from_email = settings.EMAIL_HOST_USER  # ایمیل فرستنده
    main_email = 'tvoxy2025@gmail.com'
    send_mail(
        subject,
        message,
        from_email,
        [main_email],  # لیست دریافت‌کنندگان
        fail_silently=False,
    )