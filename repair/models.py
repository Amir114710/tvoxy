from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from account.models import User
from django.utils.text import slugify


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
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)

class CategoryMobile(models.Model):
    title = models.CharField(max_length=1500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)

class MobileRepair(models.Model):
    repair = models.ForeignKey(Repair , on_delete=models.CASCADE , related_name='mobile_repair')
    categories = models.ManyToManyField(CategoryMobile , related_name='mobile_repair_category')
    slug = models.SlugField(null=True , unique=True , blank=True)
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
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(MobileRepair , self).save()

    class Meta:
        ordering = ('-created',)

class Comment(models.Model):
    user = models.ForeignKey(User , related_name="comment" , on_delete=models.CASCADE)
    mobile_repair = models.ForeignKey(MobileRepair , related_name="comment" , on_delete=models.CASCADE)
    message = RichTextUploadingField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}-{self.mobile_repair.title}'

    class Meta:
        ordering = ('-created',)

class RepairInfoModel(models.Model):
    title = models.CharField(max_length=1500)
    content = RichTextUploadingField(help_text='more info about repair')
    image = models.ImageField(upload_to='about_us/image')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)

class RepairAttributes(models.Model):
    title = models.CharField(max_length=500)
    first_word = models.CharField(max_length=5 , help_text='first word on title')
    content = RichTextUploadingField(null=True , blank=True)
    image = models.TextField(help_text='image of attributes')
    link = models.TextField(help_text='linke to read more about this attributes')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title[:10]
    
    class Meta:
        ordering = ('-created',)

class Brand(models.Model):
    title = models.CharField(max_length=2500)
    image = models.ImageField(upload_to='repair/image/brand')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)

class RepairKind(models.Model):
    title = models.CharField(max_length=550 , null=True , blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)

class DateTimeModel(models.Model):
    day = models.CharField(max_length=550 , null=True , blank=True)
    time = models.TimeField(null=True , blank=True)
    quantity = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.day}-{self.time}'
    
    class Meta:
        ordering = ('-created',)

class Reservation(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True)
    day_time = models.CharField(max_length=1050 , null=True , blank=True)
    repair_kind = models.CharField(max_length=650 , null=True , blank=True)
    model_phone = models.CharField(max_length=580 , null=True , blank=True)
    Full_name = models.CharField(max_length=580 , null=True , blank=True)
    phone_number = models.CharField(max_length=580 , null=True , blank=True)
    description = models.TextField(null=True , blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.day_time}-{self.repair_kind}-{self.model_phone}'
