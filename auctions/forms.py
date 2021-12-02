from django.forms import ModelForm
from .models import User, Auction_Listings
from django import forms

class Auction_ListingsForm(ModelForm):
    class Meta:
        model = Auction_Listings
        fields = ['title', 'description', 'starting_bid', 'image_file', 'image_url' ]
