from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class AboutCharity(models.Model):
    title = models.CharField(max_length=1500)
    content = RichTextUploadingField(help_text='more info about joband web site')
    image = models.ImageField(upload_to='business/image')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)

class CharityAttr(models.Model):
    title = models.CharField(max_length=850)
    content = RichTextUploadingField(help_text='more info about service attr')
    image = models.TextField(null=True , blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)

class Charity(models.Model):
    first_name = models.CharField(max_length=2500)
    last_name = models.CharField(max_length=2500)
    company_name = models.CharField(max_length=2500)
    company_type = models.CharField(max_length=2500)
    email = models.EmailField()
    phone = models.BigIntegerField(default=0)
    address = models.TextField()
    discription = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
    
    class Meta:
        ordering = ('-created',)