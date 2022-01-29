from unicodedata import name
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("forgetpassword", views.forgetpassword, name="forgetpassword"),
    path("blog", views.blog, name="blog"),
    path("create", views.create, name="create"),
    path("contact", views.contact, name="contact"),
]