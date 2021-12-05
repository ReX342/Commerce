from django.forms import ModelForm
from .models import User, Auction_Listings, WatchList
from django import forms

class Auction_ListingsForm(ModelForm):
    class Meta:
        model = Auction_Listings
        fields = ['title', 'description', 'starting_bid', 'image_file', 'image_url', 'quantity' ]

class WatchListForm(ModelForm):
    watch_form = forms.BooleanField(initial=True)
    class Meta:
        model = WatchList
        fields = ['watching', 'watch_form']
    # stuck on init bug
    # def __init__(self, *args, **kwargs):
    # #        Watchlist = kwargs.pop('Watchlist')
    #     super(Auction_ListingsForm, self).__init__(*args, **kwargs)