# --------------------------------------------------------- Methods
from django.shortcuts import render, redirect
from django.http import HttpResponse
# --------------------------------------------------------- Auth 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# --------------------------------------------------------- Models, Forms
from .models import Profile
from .forms import ProfileForm


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

# --------------------------------------------------------- Login


# --------------------------------------------------------- Dashboard

def dashboard(request):
    return render(request, 'dashboard.html')

# --------------------------------------------------------- Browse

def browse(request):
    return render(request, 'browse.html')

# --------------------------------------------------------- User Public


# --------------------------------------------------------- Item Details


# --------------------------------------------------------- Add Item Form


# --------------------------------------------------------- Add Reservation Form


# --------------------------------------------------------- Reservation Details