from django.urls import path
from . import views

urlpatterns = [
    
# -------------------------------------------------------------------   Home
    
    path('',views.home, name='home'),

# -------------------------------------------------------------------  Profiles

    path('accounts/signup',views.signup, name='signup'),
    
    path('profile/<int:profile_id>',views.profile,name='profile'),

    path('profile/<int:profile_id>/edit', views.edit_profile, name='edit_profile'),

    path('profile/delete', views.delete_profile, name='delete_profile'),

# -------------------------------------------------------------------   Dashboard
    
    path('dashboard/', views.dashboard, name='dashboard'),

# -------------------------------------------------------------------   Browse
    
    path('browse/', views.browse, name='browse'),

    path('browse/<int:cat_id>', views.browse_cat, name='browse_cat'),

    path('browse/loc/<int:loc_id>', views.browse_loc, name='browse_loc'),

    path('browse/loc/<int:loc_id>/cat/<int:cat_id>', views.browse_loc_cat, name='browse_loc_cat'),

# -------------------------------------------------------------------   Items

    path('items/new', views.add_item, name='add_item'),

    path('items/<int:item_id>', views.item_detail, name='item_detail'),

    path('items/<int:item_id>/edit', views.item_edit, name='item_edit'),

    path('items/<int:item_id>/delete', views.item_delete, name='item_delete'),


# -------------------------------------------------------------------   Reservations

    path('items/<int:item_id>/rez/new', views.add_rez, name='add_rez'),

    path('rez/<int:rez_id>', views.rez_detail, name='rez_detail'),

    path('rez/<int:rez_id>/edit', views.rez_edit, name='rez_edit'),

    path('myrez/<int:rez_id>/edit', views.rez_edit_owner, name='rez_edit_owner'),

    path('rez/<int:rez_id>/delete', views.rez_delete, name='rez_delete'),


# -------------------------------------------------------------------   Reviews

    path('items/<int:item_id>/review/new', views.add_review, name='add_review'),

    path('reviews/<int:rev_id>/edit', views.edit_review, name='edit_review'),
    
    path('reviews/<int:rev_id>/delete', views.delete_review, name='delete_review'),


]