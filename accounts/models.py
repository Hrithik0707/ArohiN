from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from PIL import Image
from django.conf import settings

# For creating User
class UserAccountManager(BaseUserManager):
    # For creating Application user
    def create_user(self, phone_number,password=None, **extra_fields):
        if not phone_number:
            raise ValueError('phone number must be set!')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
    
        user.save(using=self._db)
        return user

    # For creating superuser
    def create_superuser(self, phone_number,password):
        user = self.create_user(phone_number,password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

 # User Model - For creating users  
class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.IntegerField(
        unique=True,
    )
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    profile_picture = models.ImageField(default='images/avatar.png',upload_to='images/',null=True,blank=True)
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

# Product Model - for storing products by different users
class Product(models.Model):
    user=models.ForeignKey( User,on_delete=models.CASCADE) 
    shop_name = models.CharField(max_length=50) 
    product_img = models.ImageField(upload_to='product_images/') 
    shop_address = models.CharField( max_length=100)
    product_desc = models.TextField()
    product_rating = models.FloatField(null=True,blank=True)
    product_cost = models.IntegerField()
    product_name = models.CharField( max_length=50)
    product_category = models.CharField( max_length=50)
    product_id = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return str(self.product_name)

# Category Model - for storing various categories
class Category(models.Model):
    category_title = models.CharField(max_length=20)
    category_img = models.ImageField(upload_to='category_images/')
    products_count = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.category_title)


    
    

    
