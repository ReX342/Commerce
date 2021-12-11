from django.forms import ModelForm, Textarea
from .models import User, Auction_Listings, comments_AL
from django import forms

class Auction_ListingsForm(ModelForm):
    class Meta:
        model = Auction_Listings
        fields = ['title', 'description', 'category', 'starting_bid', 'image_file', 'image_url', 'quantity' ]
