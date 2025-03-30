from django.db import models
from account.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify


class Tag(models.Model):
    title = models.CharField(max_length=2500 , null=True)
    
    def __str__(self):
        return self.title
    
class Category(models.Model):
    title = models.CharField(max_length=2500 , null=True)

    def __str__(self):
        return self.title
    
class Tip(models.Model):
    tip = models.TextField(null=True)
    
    def __str__(self):
        return self.tip
    
class Article(models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE , related_name='articles')
    category = models.ManyToManyField(Category , related_name='articles_cate')
    tag = models.ManyToManyField(Tag , related_name='article_tag')
    tip = models.ManyToManyField(Tip , related_name='article_tip')
    title = models.CharField(max_length=2500 , null=True)
    slug = models.SlugField(null=True , blank=True)
    little_discription = RichTextUploadingField()
    discription = RichTextUploadingField()
    image = models.FileField(upload_to='blog/image/')
    is_publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article , self).save()
    
    class Meta:
        ordering = ('-created',)
