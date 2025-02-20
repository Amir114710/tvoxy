from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

class ServiceAttr(models.Model):
    title = models.CharField(max_length=850)
    content = RichTextUploadingField(help_text='more info about service attr')
    image = models.TextField(null=True , blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('in_progress', 'In Progress'),
    ]
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='user_service_ticket')
    subject = models.CharField(max_length=560)
    phone_model = models.CharField(max_length=560 , null=True)
    phone_brand = models.CharField(max_length=560 , null=True)
    discription = RichTextUploadingField(help_text='little information about ticket')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject[:55]
    
    class Meta:
        ordering = ('-created_at',)

class TicketMessage(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='user_message')
    ticket = models.ForeignKey(Ticket , on_delete=models.CASCADE , related_name='ticket_message')
    message = RichTextUploadingField(help_text='messages of ticket')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message[:50]
    
    class Meta:
        ordering = ('-created_at',)

class TicketAnswer(models.Model):
    ticket = models.ForeignKey(Ticket , on_delete=models.CASCADE , related_name='ticket_answer')
    message = models.ForeignKey(TicketMessage , on_delete=models.CASCADE , related_name='message_ticket')
    answer = RichTextUploadingField(help_text='answer the message')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer[:50]
    
    class Meta:
        ordering = ('-created_at',)
