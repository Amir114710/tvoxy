from django.urls import path
from .views import *

app_name = 'repair_app'

urlpatterns = [
    path('' , RepairView.as_view() , name='repair'),
    path('detail/<int:pk>' , RepairDetailView.as_view() , name='repair_detail'),
    path('mobile_repair/detail/<str:slug>' , MobileRepairDetailView.as_view() , name='mobile_repair_detail'),
]