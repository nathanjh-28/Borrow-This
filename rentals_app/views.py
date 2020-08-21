from django.shortcuts import render

from django.http import HttpResponse



#--------------------------------  Home
def home(request):
    return render(request,'home.html')


#--------------------------------  SignUp Form


#--------------------------------  Login


#--------------------------------  Dashboard

def dashboard(request):
    return render(request, 'dashboard.html')

#--------------------------------  Browse

def browse(request):
    return render(request, 'browse.html')

#--------------------------------  User Public


#--------------------------------  Item Details


#--------------------------------  Add Item Form


#--------------------------------  Add Reservation Form


#--------------------------------  Reservation Details