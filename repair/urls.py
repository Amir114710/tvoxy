from django.urls import path
from .views import *

app_name = 'repair_app'

urlpatterns = [
    path('' , RepairView.as_view() , name='repair'),
    path('detail/<int:id>' , RepairDetailView.as_view() , name='repair_detail'),
    path('mobile_repair/detail/<int:id>' , MobileRepairDetailView.as_view() , name='mobile_repair_detail'),
]