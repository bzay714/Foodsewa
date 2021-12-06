from django.db import models

class signup(models.Model):
    username = models.CharField(max_length=70)
    phonenum = models.IntegerField()
    

# restaurants
class Restaurants(models.Model):
    photo = models.FileField(upload_to="media/")
    name= models.CharField(max_length=70)
    contact = models.IntegerField()
    location= models.CharField(max_length=70)

# Menu 
x=Restaurants.objects.values_list('name')
z=[]
for i in x:
    z.append(tuple(i*2))
class Menu(models.Model):
    name = models.CharField(max_length=70)
    price = models.IntegerField()
    restaurant = tuple(z)
    Choose_restaurant = models.CharField(
        max_length=70,
        choices=restaurant,
        default='Bajeko sekuwa',
    )
