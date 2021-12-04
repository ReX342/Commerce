from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.files import File
import os


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
    # Maybe multiple relationships instead of parents/foreignkey?
    starting_bid = models.PositiveIntegerField()
    current_bid = models.PositiveIntegerField()
    def __str__(self):
        return self.starting_bid
    

class comments_AL(models.Model):
    AL = models.ForeignKey('Auction_Listings', on_delete=models.CASCADE, related_name='auction_list') 
    #foreignkey: on delete CASCADE
    # Auction_Listings is parent
    pass
# other half of https://auction-website.readthedocs.io/en/latest/4.model-layer.html
class Auction(models.Model):
    product_id = models.ForeignKey(Auction_Listings, on_delete=models.CASCADE)
    number_of_bids = models.IntegerField()
    time_starting = models.DateTimeField()
    time_ending = models.DateTimeField()

class Watchlist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)

class Bid(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bid_time = models.DateTimeField()

# We might be infiltrating error messages here instead of chat messages but whatever.    
class Chat(models.Model):
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    time_sent = models.DateTimeField()