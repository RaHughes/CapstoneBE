from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below
# In order for the new columns to appear in the database run:
# 1. python manage.py makemigrations
# 2. python manage.py migrate


class User(AbstractUser):
    middle_name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    
class Business(models.Model):
    title = models.CharField(max_length=200)
    ownerId = models.IntegerField()
    description = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

class Message(models.Model):
    to_userId = models.IntegerField()
    from_userId = models.IntegerField()
    message = models.CharField(max_length=1000)
        