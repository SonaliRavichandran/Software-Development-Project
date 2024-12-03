from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile  # Assuming you have a Profile model to store extra user details
from .models import EventBooking

# Create a custom form by extending the built-in UserCreationForm
class UserCreationFormWithProfile(UserCreationForm):
    # Add extra fields to the form
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=10, required=True)  # You can use more complex validation if needed

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  # Use the default fields from UserCreationForm
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('name')
        user.email = self.cleaned_data.get('email')
        if commit:
            user.save()
        
        # Create a profile instance to store the phone number (and any other additional fields)
        profile = Profile.objects.create(user=user, phone=self.cleaned_data.get('phone'))
        return user



class EventBookingForm(forms.ModelForm):
    class Meta:
        model = EventBooking
        fields = ['name', 'email', 'phone', 'seating', 'tickets']


class PaymentForm(forms.Form):
    card_name = forms.CharField(max_length=100, label="Cardholder's Name")
    card_number = forms.CharField(max_length=16, label="Card Number", widget=forms.TextInput(attrs={'placeholder': 'XXXX-XXXX-XXXX-XXXX'}))
    expiry_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'month'}), label="Expiry Date")
    cvv = forms.CharField(max_length=3, label="CVV", widget=forms.PasswordInput(attrs={'placeholder': 'XXX'}))