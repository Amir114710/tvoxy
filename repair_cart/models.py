from django.db import models
from account.models import User
from datetime import datetime
from repair.models import MobileRepair

class Order(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='orders')
    total_price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_pay = models.BooleanField(default=False)
    addresses = models.TextField(blank=True , null=True)
    image_payed = models.FileField(upload_to='pay/image', null=True , blank=True)
    DeliveryDate = models.DateTimeField(null=True , blank=True)

    def __str__(self) -> str:
        return self.user.phone
    
    class Meta:
        ordering = ("-created_at",)

class OrderItem(models.Model):
    order = models.ForeignKey(Order , on_delete=models.CASCADE , related_name='items')
    mobile_repair = models.ForeignKey(MobileRepair , on_delete=models.CASCADE , related_name='items')
    quantity = models.SmallIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.order.user.phone
    


class DiscountCode(models.Model):
    name = models.CharField(max_length=100 , unique=True)
    discount = models.SmallIntegerField(default=0)
    quantity = models.SmallIntegerField(default=1)

    def __str__(self) -> str:
        return self.name



