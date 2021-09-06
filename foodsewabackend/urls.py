from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
     path('',views.index,name='home'),
     path('signup/',views.register,name='Signup'),
     path('signin/',views.signin,name='Signin'),
     path('restaurant/', views.addRestaurant,name="Restaurants"),
     path('deletedata/<int:id>/', views.deletefun,name="deletedata"),
     path('<int:id>/', views.update,name="update"),
     path('menu/',views.addMenu,name='menu'),
     path('deletemenu/<int:id>/', views.deleteMenu,name="deletemenu"),
     path('updatemenu/<int:id>/', views.updateMenu,name="updateMenu"),
     path('contactus/',views.contact, name='contactus'),
]
   
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)