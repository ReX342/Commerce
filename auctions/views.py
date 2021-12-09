from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Auction_Listings, User, Bids, Bid
from .forms import Auction_ListingsForm, BidsForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    listings = Auction_Listings.objects.all()    
    return render(request, "auctions/index.html", { 
                                                   "listings":listings,
                                                   })
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create(request):
    form = Auction_ListingsForm   
    #    
    if request.method == 'POST':
        form = Auction_ListingsForm(request.POST, request.FILES)
        if form.is_valid():             
            title  = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            starting_bid = form.cleaned_data["starting_bid"]
            image_url = form.cleaned_data["image_url"]
            image_file = form.cleaned_data["image_file"]            
            listing = Auction_Listings(title=title, description=description, starting_bid=starting_bid, image_url=image_url, image_file=image_file)
            listing.save()            
            return HttpResponseRedirect(reverse("index"))
        else:
            form = Auction_ListingsForm()
    else:
        form = Auction_ListingsForm()        
       
    return render(request, "auctions/create.html", {
        "form" : form
    })
    
def detail_listing(request, id):
    listing = Auction_Listings.objects.get(id=id)
    logged_in_user = User.objects.get(id=request.user.id)
    all_wish = logged_in_user.wishlisted.all()
    bids = Bid.objects.filter(listing=id).order_by('-amount')
    print(bids)
    return render(request, "auctions/listing.html", { 
                                                   "listing": listing,
                                                   "all_wish": all_wish,
                                                   "bids": bids
                                                   })

def watchlist(request):
    logged_in_user = User.objects.get(id=request.user.id)
    all_wish = logged_in_user.wishlisted.all()
    return render(request, "auctions/watchlist.html", { 
                                                "listings": all_wish,
                                                })
@login_required
def add_watch(request, id):
    logged_in_user = User.objects.get(id=request.user.id)
    listing_id = id
    logged_in_user.wishlisted.add(Auction_Listings.objects.get(id=listing_id))         
    return HttpResponseRedirect(reverse("watchmany"))

@login_required
def watchmany(request):
    listings = Auction_Listings.objects.all()
    logged_in_user = User.objects.get(id=request.user.id)
    all_wish = logged_in_user.wishlisted.all()
    return render(request, "auctions/watchmany.html", { 
                                                "listings":listings,
                                                "all_wish": all_wish
                                                })
     
@login_required    
def remove_watch(request, id):
    logged_in_user = User.objects.get(id=request.user.id)
    listing_id = id
    logged_in_user.wishlisted.remove(Auction_Listings.objects.get(id=listing_id))         
    return HttpResponseRedirect(reverse("watchlist"))

@login_required
def watch_this(request,id):
    logged_in_user = User.objects.get(id=request.user.id)
    listing_id = id
    logged_in_user.wishlisted.add(Auction_Listings.objects.get(id=listing_id))         
    return HttpResponseRedirect(reverse("watchlist"))
  
@login_required
def unwatch_this(request,id):
    logged_in_user = User.objects.get(id=request.user.id)
    listing_id = id
    logged_in_user.wishlisted.remove(Auction_Listings.objects.get(id=listing_id))         
    return HttpResponseRedirect(reverse("watchlist"))

@login_required
def bids(request, id):
    # get Auction_Listings.current_bid
    # in a nice form where user(id=id) can update
    logged_in_user = User.objects.get(id=request.user.id)
    AL = Auction_ListingsForm   
    bids = BidsForm()
    st_bid = Bids
    if request.method == 'POST':
        bids = BidsForm(request.POST)
        current_bid = AL.current_bid
        starting_bid = AL.starting_bid

        if current_bid > starting_bid:
            if bids.is_valid():             
                bids.save()            
            return HttpResponseRedirect(reverse("index"))
        else:
            bids = BidsForm()
       
    return render(request, "auctions/watch.html", {
        "bids" : bids
    })

#I give up: listing.html url bids as alternative
@login_required
def bid(request, id):
    logged_in_user = User.objects.get(id=request.user.id)
    AL = Auction_ListingsForm   
    bids = BidsForm()
    st_bid = Bids
    
    bids = BidsForm(request.POST)
    current_bid = BidsForm.current_bid
    current = Bids.objects.get(current_bid=request.current_bid)
    if request.method == 'POST':
        bids = BidsForm(request.POST)
        current_bid = st_bid.current_bid
        starting_bid = st_bid.starting_bid
        if current_bid > starting_bid:
            if bids.is_valid():             
                bids.save()            
            return HttpResponseRedirect(reverse("index"))
        else:
            bids = BidsForm()
       
    return render(request, "auctions/watch.html", {
        "bids" : bids
    })

def bid_this(request, id):
    logged_in_user = User.objects.get(id=request.user.id)
    listing_id = id
    # logged_in_user.bid.update(Auction_Listings.objects.get(id=listing_id))         
    form = BidsForm(request.POST)
    if form.is_valid():
        current_bid = request.POST["current_bid"]             
        #current_bid  = form.cleaned_data["current_bid"]
        f = Bids(current_bid="current_bid")
        f.save()
    return HttpResponseRedirect(reverse("index"))

def compare_bids(request):
    if request == "POST":
        bids = request.POST(Bids)
        if bids.current_bid > bids.starting_bid:
            current_bid = bids.current_bid
            current_bid.save()
        else:
            # Message user (in a more user friendly way)
            return HttpResponse("Your opening bid must be higher")
        return HttpResponseRedirect(reverse("index"))
    
@login_required
def placebid(request, id):
    auction = Auction_Listings.objects.get(id=id)
    bid = Bid(listing=auction, user=User.objects.get(id=request.user.id), amount=int(request.POST['amount']))
    all_bids = Bid.objects.filter(listing=auction).order_by('-amount')
    if bid.amount > auction.starting_bid:
        if len(all_bids) > 0:
            highest_bid = all_bids[0]
            if bid.amount > highest_bid.amount:
                bid.save()
            else:
                messages.info(request, f"Your bid must be above the previous bid ({highest_bid.amount}) ")
    else:
        messages.info(request, "Your bid must be higher than starting bid")
    return HttpResponseRedirect(reverse("index"))

 


# form action="/place_bid"

# <input type="hidden" name="listing_id" value="{{ listing.id }}">
# <input type="text" name="amount">

# --- in views

# place_bid function

# Nodig
# - Huidige gebruiker (te vinden in request.user dacht ik?)
# - Huidige bod amount (te vinden in request.POST['amount']
# - Huidige listing id, om de effectieve listing te kunnen terugvinden. (te vinden in request.POST['amount']

# Stappen
# 1) Haal listing op aan de hand van id
# 2) Haal bids op van de listing (sorteer op amount)
# 3) ....

# Einde van de fucntie moet een redirect zijn naar de listing.
# Er zijn twee uitkomsten
# - bid gelukt yay
# - bid niet gelukt, geef de gebruiker een melding waarom. (not authenticated, amount too low ...)