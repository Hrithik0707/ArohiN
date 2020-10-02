from django.db import models

# Create your models here.
class Users(models.Model):
     
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.models.EmailField(max_length=254)
    password = models.CharField(widget=models.PasswordInput)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)