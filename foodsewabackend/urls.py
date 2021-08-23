from django.urls import path

from . import views

urlpatterns=[
     path('',views.index,name='home'),
     path('signup/',views.register,name='Signup'),
     path('signin/',views.signin,name='Signin'),
]
   
