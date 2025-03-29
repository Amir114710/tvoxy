from django.urls import path
from .views import *

app_name = 'business_app'

urlpatterns = [
    path('' , BusinessView.as_view() , name='business'),
    path('business_form' , BusinessFormView.as_view() , name='business_form'),
]