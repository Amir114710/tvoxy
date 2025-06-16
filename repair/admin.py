from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(CategoryMobile)
admin.site.register(Repair)
admin.site.register(MobileRepair)
admin.site.register(Comment)