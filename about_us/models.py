from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class AboutInfo(models.Model):
    title = models.CharField(max_length=1500)
    content = RichTextUploadingField(help_text='more info about joband web site')
    image = models.ImageField(upload_to='about_us/image')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)

class Team(models.Model):
    name = models.CharField(max_length=950)
    image = models.ImageField(upload_to='about_us/image/team')
    twitter = models.TextField(help_text='twitter links')
    facebook = models.TextField(help_text='facebook links')
    google = models.TextField(help_text='google links')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-created',)

class Brand(models.Model):
    title = models.CharField(max_length=2500)
    image = models.ImageField(upload_to='about_us/image/brand')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)