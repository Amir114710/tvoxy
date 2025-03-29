from django.urls import path
from .views import *

app_name = 'about_us_app'

urlpatterns = [
    path('' , AboutUsView.as_view() , name='about_us'),
    path('comeing_soon' , ComeingSoon.as_view() , name='comeing_soon'),
]