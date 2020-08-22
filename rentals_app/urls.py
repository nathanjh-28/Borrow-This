from django.urls import path
from . import views

urlpatterns = [
    
# ---------------------------------------------------------  Home
    
    path('',views.home, name='home'),

# ---------------------------------------------------------  SignUp Form

    path('accounts/signup',views.signup, name='signup'),
    
# ---------------------------------------------------------  Dashboard
    
    path('dashboard/', views.dashboard, name='dashboard'),

# ---------------------------------------------------------  Public Profile

    path('profile/',views.profile,name='profile'),

# ---------------------------------------------------------  Browse
    
    path('browse/', views.browse, name='browse'),

# ---------------------------------------------------------  Add Item Form

    path('items/new', views.add_item, name='add_item'),

# ---------------------------------------------------------  Item Details

    path('items/detail', views.item_detail, name='item_detail'),

# ---------------------------------------------------------  Add Reservation Form

    path('rez/new', views.add_rez, name='add_rez'),

# ---------------------------------------------------------  Reservation Details

    path('rez/detail', views.rez_detail, name='rez_detail'),

    # TBD Update Res, Update Item, Update profile
    # TBD page for past reservations rather than on the dashboard



]