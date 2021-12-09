from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("auction/<int:id>", views.detail_listing, name="detail"),
    path("watchlist/", views.watchlist, name="watchlist"),
    path("add_watch/<int:id>", views.add_watch, name="add_watch"),
    path("watchmany", views.watchmany, name="watchmany"),
    path("remove_watch/<int:id>", views.remove_watch, name="remove_watch"),
    path("watch_this/<int:id>", views.watch_this, name="watch_this"),
    path("unwatch_this/<int:id>", views.unwatch_this, name="unwatch_this"),
    path("bid/<int:id>", views.bid, name="bid"),
    path("bids/<int:id>", views.bids, name="bids"),
    path("bid_this/<int:id>", views.bid_this, name="bid_this"),
    path("compare_bids/<int:id>", views.compare_bids, name="compare_bids"),
    path('placebid/<int:id>', views.placebid, name="placebid")
]
