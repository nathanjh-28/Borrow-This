from django import forms
from .models import Profile, Rental_Item, Reservation, Review

class DateInput(forms.DateInput):
    input_type = 'date'

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

from django.core.validators import MaxValueValidator

# -- https://stackoverflow.com/questions/22846048/django-form-as-p-datefield-not-showing-input-type-as-date

# -- https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/datetime#:~:text=The%20HTML%20%3Cinput%20type%3D%22,no%20longer%20supported%20in%20browsers.

# ---------------------------------------------------------  Profile Form
class ProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Profile
        fields = ['email', 'first_name', 'last_name', 'display_name', 'location','bio']
        email = forms.EmailField()

# ---------------------------------------------------------  Item Form
class RentalItemForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Rental_Item
        fields = ['category', 'location','title','description','picture','link','available','price','replacement_value', 'min_rental']

# ---------------------------------------------------------  Reservation Form for Renter

class ReservationForm(forms.ModelForm):
    # occasion = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
    class Meta:
        model = Reservation
        fields = ['occasion', 'start_date', 'pick_up','end_date', 'drop_off',]
        widgets = {
            'occasion': forms.TextInput(attrs = {
                'class':'occasion-input'
                }),
            'start_date': DateInput(),
            'end_date': DateInput(),
            'pick_up': DateTimeInput(),
            'drop_off': DateTimeInput(),
        }

# ---------------------------------------------------------  Reservation Form for Owner

class OwnerReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['approved', 'picked_up','returned_date', 'ready_for_pickup']
        widgets = {
            'returned_date':DateTimeInput(),
        }




# ---------------------------------------------------------  Reviews


class ReviewForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea)
    stars = forms.IntegerField(validators=[MaxValueValidator(5)])
    class Meta:
        model = Review
        fields = ['title', 'stars', 'body']

