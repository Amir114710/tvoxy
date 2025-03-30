from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=1500)
    email = models.EmailField(null=True)
    message = models.TextField()

    def __str__(self):
        return self.name
    