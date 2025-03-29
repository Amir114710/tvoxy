from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from .managers import UserManager

class User(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True
    )
    username = models.CharField(max_length=200, unique=True , null=True, blank=True)
    phone = models.CharField(max_length=12 , default='0')
    image = models.ImageField(upload_to='UserImage' , null=True, blank=True)
    Full_name = models.CharField(max_length=200 , null=True, blank=True)
    postal_code = models.CharField(max_length=11)
    is_Accept_terms = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['']

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
class OTP(models.Model):
    token = models.CharField(max_length=12 , null=True)
    email = models.EmailField(max_length=12)
    is_Accept_terms = models.BooleanField(default=False)
    code = models.SmallIntegerField(null=True, blank=True)
    expiration_date =  models.DateTimeField(null=True, blank=True , auto_now_add=True)

    def __str__(self):
        return self.email


class Address(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='addresses')
    fullname = models.CharField(max_length=100)
    address = models.TextField(null=True , blank=True)
    email = models.EmailField(null=True , blank=True)
    phone = models.CharField(max_length=12)
    postal_code = models.CharField(max_length=10)


    def __str__(self) -> str:
        return self.user.email