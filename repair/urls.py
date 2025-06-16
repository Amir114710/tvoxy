from django.urls import path
from .views import *

app_name = 'repair_app'

urlpatterns = [
    path('' , RepairView.as_view() , name='repair'),
    path('detail/<int:pk>' , RepairDetailView.as_view() , name='repair_detail'),
    path('mobile_repair/detail/<str:slug>' , MobileRepairDetailView.as_view() , name='mobile_repair_detail'),
    path('category/<int:pk>' , CategoryProductView.as_view() , name='category_detail'),
    path('category/mobile/<int:pk>' , CategoryMobileProductView.as_view() , name='category_mobile_detail'),
    path('search' , SearchBox.as_view() , name='search'),
]