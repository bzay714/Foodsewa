from django.db import models

class signup(models.Model):
    username = models.CharField(max_length=70)
    phonenum = models.IntegerField()
    