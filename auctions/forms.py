from django.forms import ModelForm
from .models import User, Auction_Listings, Bids
from django import forms

class Auction_ListingsForm(ModelForm):
    class Meta:
        model = Auction_Listings
        fields = ['title', 'description', 'category', 'starting_bid', 'image_file', 'image_url', 'quantity' ]

class BidsForm(ModelForm):
    class Meta:
        model = Bids
        fields = ['starting_bid', 'current_bid']