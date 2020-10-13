from django import forms 
from .models import Product,User
  
class ShopForm(forms.ModelForm): 
  
    class Meta: 
        model = Product 
        fields = ['shop_name', 'product_img','shop_address','product_desc','product_cost','product_rating','product_name','product_category'] 

class ProfileForm(forms.ModelForm):
      class Meta:
        model = User
        fields = ['first_name','last_name','email','address']