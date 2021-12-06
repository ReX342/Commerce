from django.forms import ModelForm
from .models import User, Auction_Listings, WatchList, Bids
from django import forms

class Auction_ListingsForm(ModelForm):
    class Meta:
        model = Auction_Listings
        fields = ['title', 'description', 'category', 'starting_bid', 'image_file', 'image_url', 'quantity' ]

class WatchListForm(ModelForm):
    watch_form = forms.BooleanField(initial=True)
    class Meta:
        model = WatchList
        fields = ['watching', 'watch_form']

class BidsForm(ModelForm):
    class Meta:
        model = Bids
        fields = ['starting_bid', 'current_bid']