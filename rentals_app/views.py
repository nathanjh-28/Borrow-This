# ------------------------------------------------------------------- Methods
from django.shortcuts import render, redirect
from django.http import HttpResponse
# ------------------------------------------------------------------- Auth 
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
# ------------------------------------------------------------------- Models, Forms
from .models import Profile, Rental_Item, Reservation
from .forms import ProfileForm, RentalItemForm, ReservationForm


#____________________________________________________________________

#_______________________     View Functions    ______________________

#____________________________________________________________________


# ------------------------------------------------------------------- Home
def home(request):
    return render(request,'home.html')

# ------------------------------------------------------------------- SignUp Form

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile_form = ProfileForm(request.POST)
            if profile_form.is_valid():
                new_profile = profile_form.save(commit=False)
                new_profile.user_id = user.id
                new_profile.save()
                login(request, user)
                return redirect('home')
        else:
            error_message = 'Invalid sign up - Try again'
    pform = ProfileForm()
    form = UserCreationForm()
    context = {
        'pform': pform,
        'form':form,
        'error_message': error_message
    }
    return render(request, 'registration/signup.html', context)

# ------------------------------------------------------------------- Dashboard

def dashboard(request):
    user = request.user
    current_profile = Profile.objects.get(user_id=user.id)
    items = Rental_Item.objects.filter(owner_id=current_profile.id)
    reservations = Reservation.objects.filter(renter_id=current_profile.id)
    context = {
        'me':current_profile,
        'items': items,
        'reservations':reservations,
    }
    return render(request, 'dashboard.html', context)

# ------------------------------------------------------------------- Edit User Profile

def edit_profile(request, profile_id):
    error_message = ''
    user = request.user
    profile = Profile.objects.get(id=profile_id)
    if request.method == 'POST':
        form = UserCreationForm(request.POST, instance=user)
        if form.is_valid():
            pform = ProfileForm(request.POST, instance=profile)
            if pform.is_valid():
                updated_user = form.save()
                updated_profile = pform.save()
                login(request, updated_user)
                return redirect('dashboard')
            else:
                error_message = 'Invalid Profile Edit'
        else:
            error_message = 'Invalid User Edit'
    else:
        form = UserCreationForm(instance=user)
        pform = ProfileForm(instance=profile)
        context = {
            'error_message':error_message,
            'form':form,
            'pform':pform,
        }
        return render(request, 'edit-profile.html', context)

# ------------------------------------------------------------------- Delete User Profile

def delete_profile(request):
    user = request.user
    logout(request, user)
    user.delete()
    return redirect('home')


# ------------------------------------------------------------------- Browse

def browse(request):
    items = Rental_Item.objects.all()
    context = {
        'items':items,
    }
    return render(request, 'browse.html', context)

# ------------------------------------------------------------------- User Public

def profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    items = Rental_Item.objects.filter(owner_id=profile.id)
    context = {
        'profile':profile,
        'items':items,
    }
    return render(request, 'public-profile.html', context)

# ------------------------------------------------------------------- Item Details

def item_detail(request, item_id):
    item = Rental_Item.objects.get(id=item_id)
    context = {
        'item':item
    }

    return render(request, 'item-details.html', context)

# ------------------------------------------------------------------- Add Item Form

def add_item (request):
    error_message = ''
    if request.method == 'POST':
        form = RentalItemForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            user = request.user
            current_profile = Profile.objects.get(user_id=user.id)
            new_item.owner_id = current_profile.id
            new_item.save()
            index = new_item.id
            return redirect('item_detail', index)
        else: error_message = form.errors
    form = RentalItemForm
    context = {
        'form':form,
        'error_message': error_message
    }
    return render(request, 'add-item.html', context)

# ------------------------------------------------------------------- Edit Item

def item_edit(request, item_id):
    item = Rental_Item.objects.get(id=item_id)
    error_message = ''
    if request.method == 'POST':
        form = RentalItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_detail', item.id)
        else:
            error_message = 'invalid'
    else: 
        form = RentalItemForm(instance = item)
        context = {
            'form':form,
            'item':item,
            'error_message':error_message,
        }
        return render(request, 'edit-item.html', context)


# ------------------------------------------------------------------- Delete Item

def item_delete(request, item_id):
    Rental_Item.objects.get(id=item_id).delete()
    return redirect('dashboard')

# ------------------------------------------------------------------- Add Reservation Form

def add_rez(request, item_id):
    error_message = ''
    item = Rental_Item.objects.get(id=item_id)
    user = request.user
    current_profile = Profile.objects.get(user_id=user.id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            new_rez = form.save(commit=False)
            new_rez.renter_id = current_profile.id
            new_rez.item_id = item.id
            new_rez.save()
            return redirect ('home')
        else:
            error_message = 'invalid'
    form = ReservationForm()
    context = {
        'form': form,
        'item': item,
        'error_message':error_message,
    }
    return render(request, 'add-reservation.html', context)

# ------------------------------------------------------------------- Reservation Details

def rez_detail(request, rez_id):
    reservation = Reservation.objects.get(id=rez_id)
    context = {
        'rez':reservation
    }
    return render(request, 'reservation-detail.html', context)

# ------------------------------------------------------------------- Reservation Edit

def rez_edit(request, rez_id):
    error_message = ''
    reservation = Reservation.objects.get(id=rez_id)
    item = Rental_Item.objects.get(id=reservation.item_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('rez_detail', reservation.id)
        else:
            error_message = 'Invalid'
    else:
        form = ReservationForm(instance=reservation)
        context = {
            'form': form,
            'item': item,
            'rez': reservation,
            'error_message':error_message,
        }
        return render(request, 'edit-reservation.html', context)

# ------------------------------------------------------------------- Reservation Delete

def rez_delete(request, rez_id):
    Reservation.objects.get(id=rez_id).delete()
    return redirect('browse')