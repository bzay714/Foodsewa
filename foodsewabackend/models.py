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
try:
    x=Restaurants.objects.values_list('name')
    z=[]
    for i in x:
        z.append(tuple(i*2))

except:
    z = [("empty","empty")]
class Menu(models.Model):
    name = models.CharField(max_length=70)
    price = models.IntegerField()
    restaurant = tuple(z)
    Choose_restaurant = models.CharField(
        max_length=70,
        choices=restaurant,
        default='Bajeko sekuwa',
    )

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return self.first_name + " " + self.last_name + " - " + self.email