from django.urls import path
from . import views

urlpatterns = [
    
# ---------------------------------------------------------  Home
    
    path('',views.home, name='home'),

#____________________________________________________________________

#_______________________     User Stuff    __________________________

#____________________________________________________________________

# -------------------------------------------------------------------  SignUp Form

    path('accounts/signup',views.signup, name='signup'),
    
# -------------------------------------------------------------------   Dashboard
    
    path('dashboard/', views.dashboard, name='dashboard'),

# -------------------------------------------------------------------   Public Profile

    path('profile/<int:profile_id>',views.profile,name='profile'),

#____________________________________________________________________

#_______________________     ITEMS and BROWSE    ____________________

#____________________________________________________________________

# -------------------------------------------------------------------   Browse
    
    path('browse/', views.browse, name='browse'),

# -------------------------------------------------------------------   Add Item Form

    path('items/new', views.add_item, name='add_item'),

# -------------------------------------------------------------------   Item Details

    path('items/<int:item_id>', views.item_detail, name='item_detail'),

# -------------------------------------------------------------------   Item Delete

    path('items/<int:item_id>/delete', views.item_delete, name='item_delete'),

#____________________________________________________________________

#_______________________     RESERVATIONS    ________________________

#____________________________________________________________________

# -------------------------------------------------------------------   Add Reservation Form

    path('items/<int:item_id>/rez/new', views.add_rez, name='add_rez'),

# -------------------------------------------------------------------   Reservation Details

    path('rez/<int:rez_id>', views.rez_detail, name='rez_detail'),

    # TBD Update Res, Update Item, Update profile
    # TBD page for past reservations rather than on the dashboard



]