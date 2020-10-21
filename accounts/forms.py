from django import forms 
from .models import Product,User
  
 

# Form for showing profile of user
class ProfileForm(forms.ModelForm):
      class Meta:
        model = User
        fields = ['first_name','last_name','profile_picture','email','address']