from django.urls import path
from .views import *

app_name = 'service_app'

urlpatterns = [
    path('' , ServiceAttrView.as_view() , name='service_attr'),
    path('ticket_message/create/<int:id>' , TicketMessageCreateView.as_view() , name='ticket_message_create'),
    path('ticket' , TicketListView.as_view() , name='ticket_list'),
    path('create_ticket' , CreateTicket.as_view() , name='create_ticket'),
    path('delete_ticket/<int:pk>' , TicketDeleteView.as_view() , name='delete_ticket'),
]