from django.contrib import admin
from .models import User, Auction_Listings, Bids, comments_AL, Auction, Chat, Watchlist, Bid

# Register your models here.
admin.site.register(User)
admin.site.register(Auction_Listings)
admin.site.register(Bids)
admin.site.register(comments_AL)
# https://auction-website.readthedocs.io/en/latest/4.1.admin.html
admin.site.register(Auction)
admin.site.register(Chat)
admin.site.register(Watchlist)
admin.site.register(Bid)