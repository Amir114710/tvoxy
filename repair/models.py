from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=1500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)

class Repair(models.Model):
    title = models.CharField(max_length=2500)
    image = models.ImageField(upload_to='repair/images')
    categories = models.ManyToManyField(Category , related_name='repair_category')
    price = models.BigIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)

class MobileRepair(models.Model):
    repair = models.ForeignKey(Repair , on_delete=models.CASCADE , related_name='mobile_repair')
    categories = models.ManyToManyField(Category , related_name='mobile_repair_category')
    title = models.CharField(max_length=1500)
    image = models.ImageField(upload_to='repair/images')
    little_content = RichTextUploadingField()
    content = RichTextUploadingField()
    price = models.BigIntegerField(default=1)
    status = models.BooleanField(default=True)
    on_sale = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)

class Comments(models.Model):
    user = models.ForeignKey(User , related_name="comment" , on_delete=models.CASCADE)
    mobile_repair = models.ForeignKey(MobileRepair , related_name="comment" , on_delete=models.CASCADE)
    message = RichTextUploadingField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}-{self.mobile_repair.title}'

    class Meta:
        ordering = ('-created',)