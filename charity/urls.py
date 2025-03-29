from django.urls import path
from .views import *

app_name = 'charity'

urlpatterns = [
    path('' , CharityView.as_view() , name='charity_main'),
    path('charity_form' , CharityFormView.as_view() , name='charity_form'),
]