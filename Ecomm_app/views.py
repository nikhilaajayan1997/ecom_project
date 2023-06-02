from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request,'login.html')

def home_page(request):
    return render(request,'home.html')

def aboutus(request):
    return render(request,'about.html')

def aboutus1(request):
    return render(request,'about1.html')

def contactus(request):
    return render(request,'contact.html')

def contactus1(request):
    return render(request,'contact1.html')

def details(request):
    return render(request,'details.html')

def details1(request):
    return render(request,'details1.html')

def sign_up(request):
    return render(request,'sign_up.html')

def gallery(request):
    return render(request,'gallery.html')

def user_home(request):
    return render(request,'home1.html')

def user_signup(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        user=User.objects.create_user(first_name=first_name,last_name=last_name,
                                           email=email,username=username,password=password)

        user.save()
        return redirect('home')

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                auth.login(request,user)
                return redirect('admin_home')
            else:
                auth.login(request,user)
                return redirect('user_home')
    else:
        messages.info(request,'invalid credentials')
        return redirect('home_page')

def cart(request):
    return render(request,'cart.html')
        
