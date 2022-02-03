from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')
def forgetpassword(request):
    return render(request, 'forgetpassword.html')
def blog(request):
    return render(request, 'blog.html')
def create(request):
    return render(request, 'create.html')
def contact(request):
    return render(request, 'contact.html')