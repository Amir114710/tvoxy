from django.urls import path
from .views import *

app_name = 'service_app'

urlpatterns = [
    path('' , ServiceAttrView.as_view() , name='service_attr'),
    path('service_form' , ServiceFormView.as_view() , name='service_form'),
]