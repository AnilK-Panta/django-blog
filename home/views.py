import datetime
from os import curdir
from urllib import response
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate
from home.models import Blog
from django.contrib.auth.decorators import login_required

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
    blogs=Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})

def contact(request):
    return render(request, 'contact.html')
def blogview(request,id, *args, **kwargs):
    blog = Blog.objects.get(id=id)
    return render(request, "blog-view.html", {'blog': blog})

@login_required(login_url='login')
def create(request):
    if request.method=="POST":
        tag=request.POST['tag']
        title=request.POST['title']
        curdate=datetime.date.today()
        descr=request.POST['description']
        if(title!="" and descr!="" and tag!=""):
            blogpost=Blog(tag=tag, title=title, curdate=curdate, descr=descr)
            blogpost.save()
            return redirect("blog")
        else:
            messages.info(request, "Please Enter the field before submitting")
            return redirect("create")
        
    else:
        return render(request, 'create.html')