from django.db import models

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from PIL import Image
from django.conf import settings
# Create your models here.
class UserAccountManager(BaseUserManager):
    def create_user(self, phone_number,password=None, **extra_fields):
        if not phone_number:
            raise ValueError('phone number must be set!')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
    
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number,password):
        user = self.create_user(phone_number,password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    



class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.IntegerField(
        unique=True,
    )
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def get_by_natural_key(self, phone_number):
        return self.get(code_number=phone_number)

    def __str__(self):
        return str(self.phone_number)

class Product(models.Model):
    user=models.ForeignKey( User,on_delete=models.CASCADE) 
    shop_name = models.CharField(max_length=50) 
    product_img = models.ImageField(upload_to='images/') 
    shop_address = models.CharField( max_length=100)
    product_desc = models.TextField()
    product_rating = models.FloatField()
    product_cost = models.IntegerField()
    product_name = models.CharField( max_length=50)
    product_category = models.CharField( max_length=50)

    def __str__(self):
        return str(self.product_name)


    
    

    
