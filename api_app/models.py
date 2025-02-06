from django.db import models
#from django.contrib.auth.models import AbstractUser
# Create your models here.

class login_api(models.Model):
    Email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    