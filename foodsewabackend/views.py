from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from .models import signup
from django.contrib import messages

# Create your views here.
def index(request):
    return HttpResponse ("Hello world")


def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        phone=request.POST['phone']
        password=request.POST['password1']
        re_pass=request.POST['password2']
        if password==re_pass and len(str(phone))==10:
            reg=signup(username=username, phonenum=phone)
            reg.save()
            user= User.objects.create_user(username=username,first_name=firstname, last_name=lastname, password = password)
            user.save()
            return HttpResponseRedirect('/signin/')
        else:
            messages.error(request, "Please enter the correct phone number")
            return HttpResponseRedirect('/signup/')
    else:
        return render (request , "register.html")

def signin(request):
    return render(request , "signin.html")

