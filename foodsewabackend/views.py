from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import signup,Restaurants, Menu
from django.contrib import messages
from . forms import RegistrationForm,MenuForm
from django.contrib.auth import authenticate, login
import os


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
            messages.success(request, "Your FoodSewa account has been successfully created. Please login to continue.")

            return HttpResponseRedirect('/signin/')
    else:
        form = RegistrationForm()
    return render (request , "register.html",{"forms": form})


def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid Credentials. Try Again Please!")
            return redirect("login")

    else:
        return render(request, "login.html")



# add and view resturant
def addRestaurant(request):
    if request.method == "POST":
        photo=request.FILES['photo']
        name=request.POST['name']
        contact=request.POST['contact']
        location=request.POST['location']
        rest=Restaurants(photo=photo, name=name,contact=contact,location=location )
        rest.save()
        messages.success(request, "Successfully Added")
        return HttpResponseRedirect("/restaurant/")
    else:
        data=Restaurants.objects.all()

    return render(request , "form.html",{'data':data})

def deletefun(request,id):
    if request.method =="POST":
        proddlt = Restaurants.objects.get(pk=id)
        proddlt.delete()
        messages.error(request, "Successfully Deleted")
        return HttpResponseRedirect("/restaurant/")


def update(request, id):
    # return render(request, 'update.html', {'id':id})
    if request.method=='POST':
        photo=request.FILES['photo']
        name=request.POST['name']
        contact=request.POST['contact']
        location=request.POST['location']
        rest=Restaurants(photo=photo, name=name,contact=contact,location=location,id=id)
        rest.save()
        return HttpResponseRedirect("/restaurant/")
    else:
        data=Restaurants.objects.get(id=id)

    return render(request, 'update.html', {'data':data})



# add and view menu
def addMenu(request):
    if request.method == "POST":
        form=MenuForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Added")
            return HttpResponseRedirect("/menu/")
    else:
        form=MenuForm()
        data=Menu.objects.all()
    return render(request , "menu.html",{'data':data,'form':form})

def deleteMenu(request,id):
    if request.method =="POST":
        print(id)
        proddlt = Menu.objects.get(pk=id)
        print(proddlt)
        proddlt.delete()
        messages.error(request, "Successfully Deleted")
        return HttpResponseRedirect("/menu/")


def updateMenu(request, id):
    if request.method == "POST":
        pk=Menu.objects.get(pk=id)
        form=MenuForm(request.POST,instance=pk)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/menu/")
    else:
        pk=Menu.objects.get(pk=id)
        form=MenuForm(instance=pk)
        return render(request , "menuupdate.html",{'form':form})


def contact(request):
    return render(request, "contactus.html")