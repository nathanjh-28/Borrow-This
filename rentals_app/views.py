# --------------------------------------------------------- Methods
from django.shortcuts import render, redirect
from django.http import HttpResponse
# --------------------------------------------------------- Auth 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# --------------------------------------------------------- Models, Forms
from .models import Profile, Rental_Item, Reservation
from .forms import ProfileForm, RentalItemForm, ReservationForm


#____________________________________________________________________

#_______________________     View Functions    ______________________

#____________________________________________________________________


# --------------------------------------------------------- Home
def home(request):
    return render(request,'home.html')

# --------------------------------------------------------- SignUp Form

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

# --------------------------------------------------------- Dashboard

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
        

# --------------------------------------------------------- Browse

def browse(request):
    items = Rental_Item.objects.all()
    context = {
        'items':items,
    }
    return render(request, 'browse.html', context)

# --------------------------------------------------------- User Public

def profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    items = Rental_Item.objects.filter(owner_id=profile.id)
    context = {
        'profile':profile,
        'items':items,
    }
    return render(request, 'public-profile.html', context)

# --------------------------------------------------------- Item Details

def item_detail(request, item_id):
    item = Rental_Item.objects.get(id=item_id)
    context = {
        'item':item
    }

    return render(request, 'item-details.html', context)

# --------------------------------------------------------- Add Item Form

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

# --------------------------------------------------------- Add Reservation Form

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

# --------------------------------------------------------- Reservation Details

def rez_detail(request, rez_id):
    reservation = Reservation.objects.get(id=rez_id)
    context = {
        'rez':reservation
    }
    return render(request, 'reservation-detail.html', context)