from django.urls import path , re_path , include
from . import views


app_name = 'account'


urlpatterns = [
    path('otp_registeration' , views.OtpRegisterationView.as_view() , name="otp"),
    path('check_otp' , views.CheckOtpCode.as_view() , name="check_otp"),
    path('logout' , views.logout_user , name="logout"),
    path('profile' , views.ProfileView.as_view() , name="profile"),
    path('edit_profile' , views.profile_edite , name="edit_profile"),
    path('add/address' , views.AddAdressView.as_view() , name="add_address"),
    path('shop/orders' , views.ShopOrderView.as_view() , name='shop_order'),
    path('repair/orders' , views.RepairOrderView.as_view() , name='repair_order'),
    path('sell/orders' , views.SellOrderView.as_view() , name='sell_order'),
    path('report' , views.ReportView.as_view() , name='report'),
]
