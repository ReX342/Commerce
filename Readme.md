Requirements:

python -m pip install Pillow

To Do:
links up bids.model


If the user is signed in, the user should be able to add the item to their “Watchlist.” If the item is already on the watchlist, the user should be able to remove it.

Check out wiki for edit Boolean in models and forms:
want same thing for watchlist: 
    Half form so we have Boolean POST, half actual description etc. (get data from model)

https://youtu.be/OgA0TTKAtqQ
4min: AJAX (HTTP_REFERER) + exist() (instead of Boolean!)
another reason to work (class) Item based (take objects from Item)
11min: https://dbdiagram.io/

Made some favorites in github of other people's succesful wishlist projects
Watch tutorial first and come back to it later without feeling lost.

25min:
urls.py
    path("wishlist/add_to_wishlist/<int:id>", views.user_wishlist, name="user_wishlist")
views.py
def add_to_wishlist(request, id):
    produect = get_object_or_404(Product, id=id)