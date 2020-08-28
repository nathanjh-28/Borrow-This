from django.db import models

#  --  I don't know
from django.urls import reverse
from datetime import date

from django.core.exceptions import ValidationError

# https://stackoverflow.com/questions/30849862/django-max-length-for-integerfield
from django.core.validators import MaxValueValidator


# -------------------------------------------------------------------  Django User Model
from django.contrib.auth.models import User

# -------------------------------------------------------------------  Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    display_name = models.CharField('Display Name', max_length=50)
    image = models.URLField(max_length=500,default=
    'https://images.unsplash.com/photo-1506551109886-6101f48c1ab9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=80')
    location = models.CharField(max_length=100)
    bio = models.CharField(max_length=2000)

    def __str__(self):
        return self.display_name
# -------------------------------------------------------------------  Location Model
class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
# -------------------------------------------------------------------  Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
# -------------------------------------------------------------------  Rental Item Model

class Rental_Item(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    picture = models.URLField('Picture (URL)', max_length=200, blank=True)
    link = models.URLField('Link To Producte Page',max_length=200,blank=True)
    available = models.BooleanField()
    price = models.DecimalField('Price Per Day', max_digits=10, decimal_places=2)
    replacement_value = models.DecimalField('Replacement Value', max_digits=10, decimal_places=2)
    min_rental = models.IntegerField('Minimum Rental Period in Days', default=1)

    def __str__(self):
        return self.title

# -------------------------------------------------------------------  Reservation Model

class Reservation(models.Model):
    occasion = models.CharField(max_length=50)
    renter = models.ForeignKey(Profile, on_delete=models.CASCADE)
    item = models.ForeignKey(Rental_Item, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    pick_up = models.DateTimeField('Choose a pick up day and time', blank=True, null=True)
    drop_off = models.DateTimeField('Choose a drop off day and time', blank=True, null=True)
    picked_up = models.BooleanField(default=False)
    returned_date = models.DateTimeField(blank=True, null=True)
    approved = models.BooleanField(default=False)
    ready_for_pickup = models.BooleanField(default=False)

    def __str__(self):
        return f"""
        Occasion: {self.occasion},
        Renter: {self.renter.display_name},
        Item: {self.item.title},
        Start:{self.start_date} 
        to 
        End {self.end_date}
        """


# -------------------------------------------------------------------  Reviews Model

class Review(models.Model):

    class Stars(models.IntegerChoices):
        One_Star = 1
        Two_Star = 2
        Three_Star = 3
        Four_Star = 4
        Five_Star = 5

    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    item = models.ForeignKey(Rental_Item, on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    stars = models.IntegerField(choices=Stars.choices)

    def __str__(self):
        return self.title



