from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
   name = models.CharField('Venue Name', max_length=120)
   address = models.CharField(max_length=300)
   zip_code = models.CharField('Zip/Post Code', max_length=12, blank=True)
   phone = models.CharField('Contact Phone', max_length=20, blank=True)
   web = models.URLField('Web Address', blank=True)
   email_address = models.EmailField('Email Address', blank=True)

   def __str__(self):
        return self.name
   
class MyClubUser(models.Model):
    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField('Last Name', max_length=30)
    email = models.EmailField('Email')
    phone = models.CharField('Phone', max_length=20)
    address = models.CharField('Address', max_length=300)
    date_joined = models.DateTimeField('Date', auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
   name = models.CharField('Event Name', max_length=120)
   event_date = models.DateTimeField('Event Date')
   venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
   manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
   description = models.TextField(blank=True)
   attendees = models.ManyToManyField(MyClubUser, blank=True)
   
   def __str__(self):
        return self.name