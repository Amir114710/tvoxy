from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.timezone import now
from account.models import User
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.title

class Product(models.Model):
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
    on_sale = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    def product_date(self):
        created = (now().date - self.created).days
        return created
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product , self).save()

    class Meta:
        ordering = ('-created',)
        get_latest_by = 'created'

class Storage(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='product_storage' , null=True)
    storage = models.CharField(max_length=2500 , null=True , blank=True)
    price = models.BigIntegerField(default=0)

    def __str__(self):
        return self.storage

class Color(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='product_color' , null=True)
    color = models.CharField(max_length=2500 , null=True)
    price = models.BigIntegerField(default=0)

    def __str__(self):
        return self.color