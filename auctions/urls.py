from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    #LoginRequiredView
    #path('page/', LoginRequiredView.as_view()),
    path('page/', login_required(views.LoginRequiredView.as_view(), login_url='register')),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
]
