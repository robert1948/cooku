from django.shortcuts import render, render, redirect
import calendar
from datetime import datetime
from calendar import HTMLCalendar
from .forms import VenueForm, EventForm
from .models import Event, Venue
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import csv
from django.views.decorators.csrf import csrf_protect

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

# Import Pagination Stuff
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Generate a PDF file Venue List
def venue_pdf(request):
    #Create a Bytestream buffer
    buf = io.BytesIO()
    # Create a canvas object
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # Create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 10)

    # Designate The Model
    venues = Venue.objects.all()
    # Add some lines of text
    lines = []
    # Loop through the data and write it to the PDF file
    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.address)
        lines.append(venue.zip_code)
        lines.append(venue.phone)
        lines.append(venue.web)
        lines.append(venue.email_address)
        lines.append(" ")

    # Loop
    for line in lines:
        textob.textLine(line)
        
    # Finish up
    textob.textLines(lines)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='venue.pdf')



# Generate Text File and CSV File
def venue_csv(request):
    venue_list = Venue.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="venue.csv"'
    # Create a CSV writer using the response object
    writer = csv.writer(response)
    # Des the model fields as the header row
    venues = Venue.objects.all()
    # Add column headings to the CSV file
    writer.writerow(['Name', 'Web', 'Address'])
    lines = []
    # Loop through the data and write it to the CSV file
    for venue in venue_list:
        writer.writerow([venue.name, venue.web, venue.address])
    return response


def venue_text(request):
    venue_list = Venue.objects.all()
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="venue.txt"'
    for venue in venue_list:
        response.write(venue.name + '\n')
        response.write(venue.web + '\n')
        response.write(venue.address + '\n\n')
    return response

def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venues')

def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('list-events')

def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-events')

    return render(request, 'events/update_event.html', {'event': event, 'form': form})

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
    event_list = Event.objects.all().order_by('name')
    return render(request, 'events/event_list.html', {'event_list': event_list})

def blog(request):
    return render(request, 'events/blog.html')

def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/show_venue.html', {'venue': venue})

def list_venues(request):
    #venue_list = Venue.objects.all().order_by('name')
    venue_list = Venue.objects.all()
    # Pagination
    p = Paginator(Venue.objects.all(), 2)
    page = request.GET.get('page')
    venues = p.get_page(page)
    return render(request, 'events/venue.html', {'venue_list': venue_list, 'venues': venues})
    #return render(request, 'events/venue.html', {'venue_list': venue_list})

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