from django import forms
from django.forms import ModelForm
from .models import Venue, Event

# Create a VenueForm class that inherits from ModelForm
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'address', 'zip_code', 'phone', 'web', 'email_address']
        labels = {
            'name': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email_address': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue address'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip/post code'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact phone'}),
            'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Web address'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email address'}),
        }

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'event_date', 'venue', 'manager', 'attendees', 'description' ]
        labels = {
            'name': '',
            'event_date': 'YYYY-MM-DD HH:MM:SS',
            'venue': 'Venue',
            'manager': 'Manager',
            'attendees': 'Attendees',
            'description': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event name'}),
            'event_date': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Event date'}),
            'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Venue'}),
            'manager': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Manager'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Attendees'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }        