from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from .models import signup
from django.contrib import messages
from . forms import RegistrationForm

# Create your views here.
def index(request):
    return HttpResponse ("Hello world")


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            phone = form.cleaned_data["phone"]
            firstname = form.cleaned_data["fname"]
            lastname = form.cleaned_data["lname"]
            password = form.cleaned_data["password1"]

            reg=signup(username=username, phonenum=phone)
            reg.save()
            user= User.objects.create_user(username=username,first_name=firstname, last_name=lastname, password = password)
            user.save()
            return HttpResponseRedirect('/signin/')
    else:
        form = RegistrationForm()
    return render (request , "register.html",{"forms": form})


def signin(request):
    return render(request , "login.html")

