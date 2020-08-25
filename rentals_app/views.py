# ------------------------------------------------------------------- Methods
from django.shortcuts import render, redirect
from django.http import HttpResponse
# ------------------------------------------------------------------- Auth 
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# ------------------------------------------------------------------- Models, Forms
from .models import Profile, Rental_Item, Reservation
from .forms import ProfileForm, RentalItemForm, ReservationForm


from .validators import get_reservations, validate_date_range



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

@login_required
def dashboard(request):
    user = request.user
    current_profile = Profile.objects.get(user_id=request.user.id)
    items = Rental_Item.objects.filter(owner_id=current_profile.id)
    reservations = Reservation.objects.filter(renter_id=current_profile.id)
    context = {
        'me':current_profile,
        'items': items,
        'reservations':reservations,
    }
    return render(request, 'dashboard.html', context)

# ------------------------------------------------------------------- Edit User Profile

@login_required
def edit_profile(request, profile_id):
    error_message = ''
    user = request.user
    profile = Profile.objects.get(id=profile_id)
    if user.id is not profile.user_id:
        return redirect('home')
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

@login_required
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
    user = request.user
    current_profile = Profile.objects.get(user_id=user.id)
    context = {
        'item':item,
        'current_profile':current_profile,
    }

    return render(request, 'item-details.html', context)

# ------------------------------------------------------------------- Add Item Form

@login_required
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

@login_required
def item_edit(request, item_id):
    item = Rental_Item.objects.get(id=item_id)
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.id is not item.owner_id:
        return redirect('home')
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

@login_required
def item_delete(request, item_id):
    item = Rental_Item.objects.get(id=item_id)
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.id is not item.owner_id:
        return redirect('home')
    item.delete()
    return redirect('dashboard')

# ------------------------------------------------------------------- Add Reservation Form

@login_required
def add_rez(request, item_id):
    error_message = ''
    item = Rental_Item.objects.get(id=item_id)
    user = request.user
    current_profile = Profile.objects.get(user_id=user.id)
    if request.method == 'POST':
        # print(f""" 
        # req.post.occasion = 
        # {request.POST['occasion']}
        # """)
        # start = int(request.POST['start_date'])
        # end = int(request.POST['end_date'])
        # print('here is my log')
        # print(type(start))
        # print(start)
        # print('end log')
        # if validate_date_range(item_id,start,end):
        #     print('good to go')
        # else:
        #     print('no way jose')
        form = ReservationForm(request.POST)
        # print(form)
        if form.is_valid():
            new_rez = form.save(commit=False)
            new_rez.renter_id = current_profile.id
            new_rez.item_id = item.id
            # print('nathan start')
            # print(type(new_rez.start_date))
            # print('nathan end')
        #     print(f"""
        #     new rez created: 
        #     {new_rez.item_id}
        #     {new_rez.start_date}
        #     {new_rez.end_date}
        #     """)
            if validate_date_range(item_id,new_rez.start_date,new_rez.end_date):
                new_rez.save()
                return redirect ('home')
            else:
                error_message = 'Conflicting Dates'
                new_rez.save()
                new_rez.delete()
                context_err = {
                    'form': form,
                    'item': item,
                    'error_message':error_message,
                    }
                return render(request, 'add-reservation.html', context_err)
        # else:
        #     error_message = 'invalid submission'
    form = ReservationForm()
    context = {
        'form': form,
        'item': item,
        'error_message':error_message,
    }
    return render(request, 'add-reservation.html', context)

# ------------------------------------------------------------------- Reservation Details

@login_required
def rez_detail(request, rez_id):
    user = request.user
    current_profile = Profile.objects.get(user_id=user.id)
    reservation = Reservation.objects.get(id=rez_id)
    context = {
        'rez':reservation,
        'current_profile':current_profile,
    }
    return render(request, 'reservation-detail.html', context)

# ------------------------------------------------------------------- Reservation Edit

@login_required
def rez_edit(request, rez_id):
    error_message = ''
    reservation = Reservation.objects.get(id=rez_id)
    item = Rental_Item.objects.get(id=reservation.item_id)
    current_profile = Profile.objects.get(user_id=request.user.id)
    if current_profile.id is not reservation.renter_id:
        return redirect ('home')
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

@login_required
def rez_delete(request, rez_id):
    reservation = Reservation.objects.get(id=rez_id)
    current_profile = Profile.objects.get(user_id=request.user.id)
    if current_profile.id is not reservation.renter_id:
        return redirect ('home')
    reservation.delete()
    return redirect('browse')

# ------------------------------------------------------------------- Test

def test(request, item_id):
    # msg = 'hello world'
    # return HttpResponse(msg)
    return HttpResponse(get_reservations(item_id))