from django.urls import path
from . import views

urlpatterns = [
    
    #--------------------------------  Home
    
    path('',views.home, name='home'),

    #--------------------------------  SignUp Form


    #--------------------------------  Login

    
    #--------------------------------  Dashboard
    
    path('dashboard/', views.dashboard, name='dashboard'),

    #--------------------------------  Browse
    
    path('browse/', views.browse, name='browse'),

    #--------------------------------  User Public


    #--------------------------------  Item Details


    #--------------------------------  Add Item Form


    #--------------------------------  Add Reservation Form


    #--------------------------------  Reservation Details



    # TBD Update Res, Update Item, Update profile
    # TBD page for past reservations rather than on the dashboard



]