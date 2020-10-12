from django import forms 
from .models import Product
  
class ShopForm(forms.ModelForm): 
  
    class Meta: 
        model = Product 
        fields = ['shop_name', 'product_img','shop_address','product_desc','product_cost','product_rating','product_name','product_category'] 