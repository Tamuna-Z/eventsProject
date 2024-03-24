from django import forms
from django.forms import ModelForm
from .models import Event
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'date_time']

class RSVPForm(forms.Form):
    pass
class CustomUserCreationForm(UserCreationForm):
    pass

class CustomAuthenticationForm(AuthenticationForm):
    pass