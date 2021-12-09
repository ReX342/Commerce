from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.files import File
import os

#from django.db.models.fields import DateTimeFields

class Auction_Listings(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=20000)
    starting_bid = models.PositiveIntegerField()
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
    host = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    active = models.BooleanField(default=True)
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


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Auction_Listings, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(null=False)
    def __str__(self):
        return f"<{self.user} bids {self.amount} on {self.listing}>"
    def __repr__(self):
        return f"<Bid '{self.user.username}' bid ' {self.amount} on {self.listing.title}'>"
    
  
class comments_AL(models.Model):
    AL = models.ForeignKey(Auction_Listings, on_delete=models.CASCADE, related_name='auction_list', unique=True) 
    user = models.ForeignKey(Auction_Listings, on_delete=models.CASCADE)
    comment = models.CharField(max_length=2000)
    def __str__(self):
        return self.AL   
