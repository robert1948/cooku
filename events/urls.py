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

]
