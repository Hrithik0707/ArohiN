from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import User,Product
from django.http import HttpResponse 
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Product,User,Category
import datetime


# Home Page
def index(request):
    return render(request,'index.html')

# Checking various fields and registering the user
def register(request):

    if request.method == 'POST':

        # Accepting all the fields from html page
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password1']
        cpassword = request.POST['password2']
        address = request.POST['address']
        phone_number = request.POST['phone_number']
        

        # Check - password n confirm password are same
        if password==cpassword:
            
            # Check - If the user with this phone no. already exists
            if User.objects.filter(phone_number=phone_number).exists():
                messages.info(request,'Phone number already available')
                return redirect('register')
            else:

                # Check - If the user with this email already exists
                if User.objects.filter(email=email).exists():
                    messages.info(request,'Email Taken')
                else:

                    # Creating user by creating object of 'User' Model
                    user = User.objects.create_user(phone_number=phone_number,password=password,email=email,first_name=first_name,last_name=last_name,address=address)
                    user.save();
                
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'Passwords not matching...')
            return redirect('register')

    else:
        return render(request,'register.html') 

# Authenticating user and loging him/her in
def login(request):
    if request.method=='POST':

        # Accepting phone no. n password from html page
        phone_number = request.POST['phone_number']
        password = request.POST['password']

        user =auth.authenticate(phone_number=phone_number,password=password)

        # Check - If the user exists
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return HttpResponse("invalid credentials")

    else:
       return render(request,'login.html')  

# For logging the user out
def logout(request):
    auth.logout(request)
    return redirect('/')

# For letting the logged user to upload post
@login_required
def upload_post(request): 
  
    if request.method == 'POST' : 
        
        # Accepting data from form for adding posts
        shop_name = request.POST['shop_name']
        product_img = request.FILES['product_img']
        shop_address = request.POST['shop_address']
        product_desc = request.POST['product_desc']
        product_cost = request.POST['product_cost']
        product_name = request.POST['product_name']
        product_category = request.POST['product_category']

        user_id=str(request.user)
        # generating product id
        product_id="post_"+str(datetime.datetime.timestamp(datetime.datetime.now()))+"_"+user_id

        prod=Product.objects.create(user=request.user,product_id=product_id,shop_name=shop_name,product_img=product_img,shop_address=shop_address,product_desc=product_desc,product_name=product_name,product_cost=product_cost,product_category=product_category)
        prod.save()
        return redirect('community_page')
    else: 
        return render(request,'postUpload.html')
  
# For response denoting success
def success(request): 
    return HttpResponse('successfully uploaded') 

# For displaying all the posts uploaded by various users
def community_page(request): 
  
    if request.method == 'GET': 
  
        # getting all the posts 
        Posts = Product.objects.all()  
        return render(request, 'display_shop_images.html',{'shop_images' : Posts})

# For displaying all the categories
def category_page(request): 
  
    if request.method == 'GET': 
  
        # getting all the categories 
        Categories = Category.objects.all()  
        return render(request, 'categories_page.html',{'categories' : Categories})

# For letting the logged in user to update his/her profile
@login_required
def profile(request):
    if request.method == 'POST':

        # Accepting data changes from Profile form
        form = ProfileForm(request.POST, request.FILES ,instance=request.user) 
        
        # Check - If the form is valid
        if form.is_valid(): 
            form.save()
            return redirect('/')
    else: 
        form = ProfileForm(instance=request.user) 
    return render(request, 'ProfileAccount.html', {'form' : form}) 
