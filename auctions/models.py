from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auction_Listings():
    pass

class Bids():
    pass

class comments_AL():
    #foreignkey: on delete CASCADE
    # Auction_Listings is parent
    pass