from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import User,Product
from django.http import HttpResponse 
from .forms import ShopForm,ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Product,User
# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        email = request.POST['email']
        password = request.POST['password1']
        cpassword = request.POST['password2']

        address = request.POST['address']
        phone_number = request.POST['phone_number']

        if password==cpassword:
            
            if User.objects.filter(phone_number=phone_number).exists():
                messages.info(request,'Phone number already available')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.info(request,'Email Taken')
                else:
                    user = User.objects.create_user(phone_number=phone_number,password=password,email=email,first_name=first_name,last_name=last_name,address=address)
                    user.save();
                
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'Passwords not matching...')
            return redirect('register')

    else:
        return render(request,'register.html') 

def login(request):
    if request.method=='POST':
        phone_number = request.POST['phone_number']
        password = request.POST['password']

        user =auth.authenticate(phone_number=phone_number,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
       return render(request,'login.html')  

def logout(request):
    auth.logout()
    return redirect('/')

@login_required
def shop_image_view(request): 
  
    if request.method == 'POST': 
        form = ShopForm(request.POST, request.FILES) 
        if form.is_valid(): 
            prod=Product.objects.create(user=request.user,shop_name=form.cleaned_data['shop_name'],product_img=form.cleaned_data['product_img'],shop_address=form.cleaned_data['shop_address'],product_desc=form.cleaned_data['product_desc'],product_name=form.cleaned_data['product_name'],product_rating=form.cleaned_data['product_rating'],product_cost=form.cleaned_data['product_cost'],product_category=form.cleaned_data['product_category'])
            prod.save()
            return redirect('shop_images')
    else: 
        form = ShopForm() 
    return render(request, 'postUpload.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfully uploaded') 

def display_shop_images(request): 
  
    if request.method == 'GET': 
  
        # getting all the objects of hotel. 
        Shops = Product.objects.all()  
        return render(request, 'display_shop_images.html',{'shop_images' : Shops})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES ,instance=request.user) 
        
        if form.is_valid(): 
            form.save()
            return redirect('/')
    else: 
        form = ProfileForm(instance=request.user) 
    return render(request, 'ProfileAccount.html', {'form' : form}) 
