from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.timezone import now
from account.models import User
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.title

class Color(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title
    
class Storage(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title
    
class Region(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=350)
    slug = models.SlugField(blank=True)
    categories = models.ManyToManyField(Category , related_name='products' , null=True , blank=True)
    color = models.ForeignKey(Color , on_delete=models.CASCADE , related_name='products_color' , null=True , blank=True)
    storage = models.ForeignKey(Storage , on_delete=models.CASCADE , related_name='products_storage' , null=True , blank=True)
    region = models.ForeignKey(Region , on_delete=models.CASCADE , related_name='products_region' , null=True , blank=True)
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

class Comments(models.Model):
    user = models.ForeignKey(User , related_name="comment_user" , on_delete=models.CASCADE)
    products = models.ForeignKey(Product , related_name="comment_mobile" , on_delete=models.CASCADE)

    parent = models.ForeignKey('self' , on_delete=models.CASCADE , related_name = 'replies' , null=True , blank=True)

    message = RichTextUploadingField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}-{self.products.title}'

    class Meta:
        ordering = ('-created',)

    def get_created(self):
        created = (now().date - self.created).days
        return created