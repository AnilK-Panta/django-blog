from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate

from home.models import Destination

# Create your views here.
def index(request):
    dests=Destination.objects.all()
    return render(request, 'index.html', {'dests': dests})
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Enter correct credintials")
            return redirect('login')
    else:
        return render(request, 'login.html')
def register(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if (password1==password2):
            if User.objects.filter(username=name).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=name, email=email, password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not matched')
            return render(request, 'register.html')    
    else:
        return render(request, 'register.html')
def logout(request):
    auth.logout(request)
    return redirect('login')
def forgetpassword(request):
    return render(request, 'forgetpassword.html')
def blog(request):
    return render(request, 'blog.html')
def create(request):
    return render(request, 'create.html')
def contact(request):
    return render(request, 'contact.html')