from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
     profilepic = models.ImageField(upload_to = 'img/',blank = True)
     shortintro = models.CharField(max_length = 200,blank=True)
