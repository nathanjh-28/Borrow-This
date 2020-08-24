from django import forms
from .models import Profile, Rental_Item, Reservation

# ---------------------------------------------------------  Profile Form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'first_name', 'last_name', 'display_name', 'location','bio']
        email = forms.EmailField()

# ---------------------------------------------------------  Item Form
class RentalItemForm(forms.ModelForm):
    class Meta:
        model = Rental_Item
        fields = ['category', 'location','title','description','picture','link','available','price','replacement_value']

# ---------------------------------------------------------  Reservation Form

# ---------------------------------------------------------  Reviews