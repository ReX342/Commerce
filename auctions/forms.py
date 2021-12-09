from django.forms import ModelForm, Textarea
from .models import User, Auction_Listings, comments_AL
from django import forms

class Auction_ListingsForm(ModelForm):
    class Meta:
        model = Auction_Listings
        fields = ['title', 'description', 'category', 'starting_bid', 'image_file', 'image_url', 'quantity' ]

class comments_ALForm(ModelForm):
    # this is the line which is used for widget, here I added TextArea widget you can see we also assigned class to widget using attrs attribute.
    comment=forms.CharField(widget=forms.Textarea(attrs={'rows':3})) 
    class Meta:
        model = comments_AL
        fields = ['AL', 'user', 'comment']