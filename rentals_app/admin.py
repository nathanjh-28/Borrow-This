from django.contrib import admin

from .models import Profile, Location, Category, Rental_Item, Reservation


# Register your models here.

admin.site.register(Profile)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Rental_Item)
admin.site.register(Reservation)

