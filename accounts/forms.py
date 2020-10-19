from django import forms 
from .models import Product,User
  
# Form for obtaining product details  
class ShopForm(forms.ModelForm): 
      class Meta: 
        model = Product 
        fields = ['shop_name', 'product_img','shop_address','product_desc','product_cost','product_name','product_category'] 

# Form for showing profile of user
class ProfileForm(forms.ModelForm):
      class Meta:
        model = User
        fields = ['first_name','last_name','profile_picture','email','address']