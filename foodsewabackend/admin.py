from django.contrib import admin
from .models import signup,Restaurants,Menu, Contact
# Register your models here.

@admin.register(signup)
class Adminsignup(admin.ModelAdmin):
    list_display = ['username','phonenum']


# restaurants
@admin.register(Restaurants)
class AdminRestaurants(admin.ModelAdmin):
    list_display = ['id','photo','name','contact','location']

# Menu
@admin.register(Menu)
class AdminMenu(admin.ModelAdmin):
    list_display = ['id','name','price','Choose_restaurant']

admin.site.register(Contact)