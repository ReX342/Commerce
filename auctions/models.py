from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.files import File
import os


class User(AbstractUser):
    pass

class Auction_Listings():
    title: models.CharField(max_length=200)
    description: models.CharField(max_length=20000)
    starting_bid: models.PositiveIntegerField()
    # add media in settings https://codedec.com/tutorials/upload-and-display-image-in-django/
    image_file = models.ImageField(upload_to='images')
    image_url = models.URLField()
    def __str__(self):
        return self.title 

class Bids():
    pass

class comments_AL():
    AL = models.ForeignKey(Auction_Listings, on_delete=models.CASCADE, related_name='auction_list') 
    #foreignkey: on delete CASCADE
    # Auction_Listings is parent
    pass