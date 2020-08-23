from django.db import models

#  --  I don't know
from django.urls import reverse
from datetime import date

# --  User Model
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)

    def __str__():
        return self.display_name



