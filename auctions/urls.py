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
    path('placebid/<int:id>', views.placebid, name="placebid"),
    path('end_auction/<int:id>', views.end_auction, name="end_auction"),
    path('new_comment/<int:id>', views.new_comment, name="new_comment"),
    path('categories', views.categories, name="categories"),
    path('categories/<str:abbr>', views.cat_list, name="cat_list")
]
