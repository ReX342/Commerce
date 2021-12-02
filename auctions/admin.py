from django.contrib import admin
from .models import User, Auction_Listings, Bids, comments_AL
# Register your models here.
admin.site.register(User)
admin.site.register(Auction_Listings)
admin.site.register(Bids)
admin.site.register(comments_AL)
