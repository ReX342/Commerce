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

 