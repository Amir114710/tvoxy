from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.timezone import now
from account.models import User
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.title
    
class SellProduct(models.Model):
    title = models.CharField(max_length=350)
    slug = models.SlugField(blank=True)
    categories = models.ManyToManyField(Category , related_name='products' , null=True , blank=True)
    price = models.BigIntegerField(default=1)
    little_discription = RichTextUploadingField(null=True , blank=True)
    main_image = models.ImageField(upload_to = 'product/image' , null=True , blank=True)
    image1 = models.ImageField(upload_to = 'product/image' , null=True , blank=True)
    image2 = models.ImageField(upload_to = 'product/image' , null=True , blank=True)
    image3 = models.ImageField(upload_to = 'product/image' , null=True , blank=True)
    image4 = models.ImageField(upload_to = 'product/image' , null=True , blank=True)
    image5 = models.ImageField(upload_to = 'product/image' , null=True , blank=True)
    image6 = models.ImageField(upload_to = 'product/image' , null=True , blank=True)
    content = RichTextUploadingField(null=True , blank=True)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    def product_date(self):
        created = (now().date - self.created).days
        return created
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(SellProduct , self).save()

    class Meta:
        ordering = ('-created',)
        get_latest_by = 'created'

class Storage(models.Model):
    sell_product = models.ForeignKey(SellProduct , on_delete=models.CASCADE , related_name='sell_storage')
    storage = models.CharField(max_length=1500)
    price = models.BigIntegerField(null=True , blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.storage
    
class Condition(models.Model):
    sell_product = models.ForeignKey(SellProduct , on_delete=models.CASCADE , related_name='sell_condition')
    condition = models.CharField(max_length=1500)
    discription = RichTextUploadingField(null=True)
    price = models.BigIntegerField(null=True , blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.condition