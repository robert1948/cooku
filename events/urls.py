from django.urls import path # Add include to the import statement
from . import views # Add this line

urlpatterns = [
    path('',views.home,name='home'), # Add this line
    path('events',views.all_events,name='list-events'), # Add this line
    path('add_venue',views.add_venue,name='add-venue'),
    path('blog',views.blog,name='blog'),
    path('firstblog',views.firstblog,name='firstblog'), 
    path('list_venues',views.list_venues,name='list-venues'),
    path('show_venue/<venue_id>',views.show_venue,name='show-venue'),
    path('search_venues',views.search_venues,name='search-venues'),
    path('update_venue/<venue_id>',views.update_venue,name='update-venue'),
    path('add_event',views.add_event,name='add-event'),
    path('update_event/<event_id>',views.update_event,name='update-event'),
    path('delete_event/<event_id>',views.delete_event,name='delete-event'),
    path('delete_venue/<venue_id>',views.delete_venue,name='delete-venue'),
    path('venue_text',views.venue_text,name='venue-text'),
    path('venue_csv',views.venue_csv,name='venue-csv'),
    path('venue_pdf',views.venue_pdf,name='venue-pdf'),
]
