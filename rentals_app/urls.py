from django.urls import path
from . import views

urlpatterns = [
    
# -------------------------------------------------------------------   Home
    
    path('',views.home, name='home'),







# -------------------------------------------------------------------  SignUp Form

    path('accounts/signup',views.signup, name='signup'),
    
# -------------------------------------------------------------------   Dashboard
    
    path('dashboard/', views.dashboard, name='dashboard'),

# -------------------------------------------------------------------   Public Profile

    path('profile/<int:profile_id>',views.profile,name='profile'),

# ------------------------------------------------------------------- Edit User Profile

    path('profile/<int:profile_id>/edit', views.edit_profile, name='edit_profile'),

# ------------------------------------------------------------------- Delete User Profile

    path('profile/delete', views.delete_profile, name='delete_profile'),







# -------------------------------------------------------------------   Browse
    
    path('browse/', views.browse, name='browse'),

# -------------------------------------------------------------------   Add Item Form

    path('items/new', views.add_item, name='add_item'),

# -------------------------------------------------------------------   Item Details

    path('items/<int:item_id>', views.item_detail, name='item_detail'),

# -------------------------------------------------------------------   Item Edit

    path('items/<int:item_id>/edit', views.item_edit, name='item_edit'),

# -------------------------------------------------------------------   Item Delete

    path('items/<int:item_id>/delete', views.item_delete, name='item_delete'),








# -------------------------------------------------------------------   Add Reservation Form

    path('items/<int:item_id>/rez/new', views.add_rez, name='add_rez'),

# -------------------------------------------------------------------   Reservation Details

    path('rez/<int:rez_id>', views.rez_detail, name='rez_detail'),

# -------------------------------------------------------------------   Reservation Edit

    path('rez/<int:rez_id>/edit', views.rez_edit, name='rez_edit'),

# -------------------------------------------------------------------   Reservation Delete

    path('rez/<int:rez_id>/delete', views.rez_delete, name='rez_delete'),




# -------------------------------------------------------------------   Test

    path('test/<int:item_id>', views.test, name='test'),



    # TBD Update Res, Update Item, Update profile
    # TBD page for past reservations rather than on the dashboard



]