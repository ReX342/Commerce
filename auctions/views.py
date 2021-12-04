from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# fixing online code copy/paste
#from django.contrib.auth.models import User
# another attempted fix: 
# # https://stackoverflow.com/questions/17873855/manager-isnt-available-user-has-been-swapped-for-pet-person
# from django.contrib.auth import get_user_model
# user = get_user_model().objects.get(pk=uid)
# queryset = get_user_model().objects.all()
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from .models import Auction_Listings, User
from .forms import Auction_ListingsForm

class LoginRequiredView(LoginRequiredMixin, TemplateView):
    
    template_name = "page.html"
    redirect_field_name = '/admin/login/?next=/admin/'
    
def index(request):
    listings = Auction_Listings.objects.all()    
    #lists = Auction_Listings.objects.open()
    return render(request, "auctions/index.html", { 
                                                   "listings":listings,
                                                   "auctions_auction_listings.quantity": 1
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
    
 
