from django.shortcuts import render, render, redirect
import calendar
from datetime import datetime
from calendar import HTMLCalendar
from .forms import VenueForm, EventForm
from .models import Event, Venue
from django.http import HttpResponseRedirect

from django.views.decorators.csrf import csrf_protect

def add_event(request):
    submitted = False
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_event.html', {'form': form, 'submitted': submitted})

def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list-venues')


    return render(request, 'events/update_venue.html', {'venue': venue, 'form': form})

@csrf_protect
def search_venues(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)       
        return render(request, 'events/search_venues.html', {'searched': searched, 'venues': venues})
    else:
        return render(request, 'events/search_venues.html', {})


# Duplicate function definition removed

def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html', {'event_list': event_list})

def blog(request):
    return render(request, 'events/blog.html')

def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/show_venue.html', {'venue': venue})

def list_venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'events/venue.html', {'venue_list': venue_list})

def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html', {'form': form, 'submitted': submitted})

def home(request):
    return render(request, 'events/home.html', {})

def vision(request):
    vision = "This is the vision content"
    return render(request, 'events/vision.html', {'vision': vision})
def show_first_blog(request):
    firstblog = "This is the first blog content"
    return render(request, 'events/firstblog.html', {'firstblog': firstblog})

def firstblog(request):
    firstblog = "This is the first blog content"
# Duplicate function definition removed