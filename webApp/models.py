from django.db import models

# Create your models here.
class User(models.Model):
    fName = models.CharField(max_length=150, default='')
    lName = models.CharField(max_length=150, default='')
    email = models.CharField(max_length=500, default='')
    password = models.CharField(max_length=250, default='')
