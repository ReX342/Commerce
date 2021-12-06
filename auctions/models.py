from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.files import File
import os

#from django.db.models.fields import DateTimeFields

class Auction_Listings(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=20000)
    starting_bid = models.PositiveIntegerField()
    #current_bid = models.PositiveIntegerField()
    image_file = models.ImageField(upload_to='images', blank=True)
    image_url = models.URLField(max_length=200, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    CATEGORIES = (
        ('LAP', 'Laptop'),
        ('CON', 'Console'),
        ('GAD', 'Gadget'),
        ('GAM', 'Game'),
        ('TEL', 'TV'),
        ('FAS', 'Fashion'),
        ('TOY', 'Toys'),
        ('ELE', 'Electronics'),
        ('HOM', 'Home')
       )
    category = models.CharField(
        max_length=45,
        choices=CATEGORIES
    )
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title 
    
    
class User(AbstractUser):
    wishlisted = models.ManyToManyField(Auction_Listings)
    def __str__(self):
        return self.username 
    def __repr__(self):
        return f"<User '{self.username}>"

class Bids(models.Model):
    starting_bid = models.PositiveIntegerField()
    current_bid = models.PositiveIntegerField()
    def __str__(self):
        return self.starting_bid
    
class comments_AL(models.Model):
    AL = models.ForeignKey('Auction_Listings', on_delete=models.CASCADE, related_name='auction_list', unique=True) 
    pass

# I can't delete these untile I delete my dbase.
class WatchList(models.Model):
    auction = models.ForeignKey('Auction_Listings', on_delete=models.CASCADE, unique=True) 
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    watching = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True, blank=True)
