from django import forms
from .models import Profile, Rental_Item, Reservation

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
        fields = ['category', 'location','title','description','picture','link','available','price','replacement_value']

# ---------------------------------------------------------  Reservation Form

class ReservationForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput)
    # occasion = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
    class Meta:
        model = Reservation
        fields = ['occasion', 'start_date', 'pick_up','end_date', 'drop_off',]
        widgets = {
            'occasion': forms.TextInput(attrs = {
                'class':'occasion-input'
                })
        }




# ---------------------------------------------------------  Reviews