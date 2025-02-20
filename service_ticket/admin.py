from django.contrib import admin
from .models import *

admin.site.register(ServiceAttr)
admin.site.register(Ticket)
admin.site.register(TicketMessage)
admin.site.register(TicketAnswer)