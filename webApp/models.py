from django.db import models

# Create your models here.
class User(models.Model):
    fName = models.CharField(max_length=15, default='')
    lName = models.CharField(max_length=15, default='')
    email = models.CharField(max_length=50, default='')
    password = models.CharField(max_length=25, default='')

