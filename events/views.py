from django.shortcuts import render
from .forms import VenueForm
from .models import Event, Venue
from django.http import HttpResponseRedirect
from django.shortcuts import render

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
    return render(request, 'events/venues.html', {'venue_list': venue_list})

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
    return render(request, 'events/firstblog.html', {'firstblog': firstblog})