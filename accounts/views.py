from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import User
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
