from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Poster(models.Model):
    title = models.CharField(max_length=500 , null=True , blank=True)
    content = RichTextUploadingField(null=True , blank=True)
    image = models.ImageField(upload_to='home/poster/image' , null=True , blank=True)
    type1 = models.BooleanField(default=False , null=True , blank=True , help_text='we can change poster style with types')
    type2 = models.BooleanField(default=False , null=True , blank=True , help_text='we can change poster style with types')
    type3 = models.BooleanField(default=False , null=True , blank=True , help_text='we can change poster style with types')
    linke = models.TextField(null=True , blank=True , help_text='links of button on posters')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ('-created',)

class CallInformation(models.Model):
    opening_time = models.CharField(max_length=250)
    call_number = models.BigIntegerField(default=0)
    gmail_us = models.EmailField(null=True , blank=True)

    def __str__(self) -> str:
        return self.gmail_us
    
class SocialMediaLinks(models.Model):
    pinterest = models.TextField(null=True , blank=True , help_text='pinterest_link')
    google = models.TextField(null=True , blank=True , help_text='google_link')
    facebook = models.TextField(null=True , blank=True , help_text='facebook_link')
    twitter = models.TextField(null=True , blank=True , help_text='twitter_link')

    def __str__(self) -> str:
        return self.google
    
class ShopAttributes(models.Model):
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

class MoreAttributes(models.Model):
    image = models.TextField(null=True , blank=True , help_text='image of Attributes')
    title = models.CharField(max_length=500 , null=True , blank=True)
    content = RichTextUploadingField(null=True , blank=True)
    link = models.TextField(null=True , blank=True , help_text='linke to read more about this attributes')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title[:10]
    
    class Meta:
        ordering = ('-created',)

class MoreDiscripUs(models.Model):
    title = models.CharField(max_length=1500)
    littel_content = RichTextUploadingField(help_text='little content about this part')
    image1 = models.ImageField(upload_to='home/morediscripUs')
    image2 = models.ImageField(upload_to='home/morediscripUs')
    image3 = models.ImageField(upload_to='home/morediscripUs')
    links = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)