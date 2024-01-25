from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        return redirect('logins')
    return render(request,'signup.html')

def logins(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("------------------username")
        print("---------------------password")
        myuser = authenticate(username=username,password=password)
        
        if myuser:
            login(request,myuser)
            return redirect('welcome_page')
    return render(request,'logins.html')

def welcome_page(request):
    return render(request,'welcome_page.html')
