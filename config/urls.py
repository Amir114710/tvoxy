from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('ckeditor/' , include('ckeditor_uploader.urls')),
    path("admin/", admin.site.urls),
    path('' , include('home.urls')),
    path('about_us/' , include('about_us.urls')),
    path('repair/' , include('repair.urls')),
    path('repair_cart/' , include('repair_cart.urls')),
    path('service/' , include('service_ticket.urls')),
    path('account/' , include('account.urls')),
    path('business/' , include('business.urls')),
    path('charity/' , include('charity.urls')),
    path('shop/' , include('shop.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)