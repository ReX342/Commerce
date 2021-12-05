from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.files import File
import os

from django.db.models.fields import DateTimeField


class User(AbstractUser):
    pass

class Auction_Listings(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=20000)
    #starting_bid = models.ForeignKey('Bids', on_delete=models.CASCADE, related_name='start_bid') 
    starting_bid = models.PositiveIntegerField()
    # add media in settings https://codedec.com/tutorials/upload-and-display-image-in-django/
    # None=True doesn't work; require
    image_file = models.ImageField(upload_to='images', blank=True)
    image_url = models.URLField(max_length=200, blank=True)
    #https://auction-website.readthedocs.io/en/latest/4.model-layer.html
    quantity = models.PositiveIntegerField(null=True, blank=True)
    CATEGORIES = (
        ('LAP', 'Laptop'),
        ('CON', 'Console'),
        ('GAD', 'Gadget'),
        ('GAM', 'Game'),
        ('TEL', 'TV')
       )
    category = models.CharField(
        max_length=45,
        choices=CATEGORIES
    )
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.title 

class Bids(models.Model):
    starting_bid = models.ForeignKey('Auction_Listings', on_delete=models.CASCADE, related_name='start_bid', primary_key=True) 
    # User on_delete=models.CASCADE
    current_bid = models.PositiveIntegerField()
    def __str__(self):
        return self.starting_bid
    
class comments_AL(models.Model):
    AL = models.ForeignKey('Auction_Listings', on_delete=models.CASCADE, related_name='auction_list', primary_key=True) 
    #foreignkey: on delete CASCADE
    # Auction_Listings is parent
    pass

class WatchList(models.Model):
    auction = models.ForeignKey('Auction_Listings', on_delete=models.CASCADE, primary_key=True ) 
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True, blank=True)