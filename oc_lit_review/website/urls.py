from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_process, name="login"),
    path("logout", views.logout_process, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("posts", views.posts, name="posts"),
    path("sub", views.subscriptions, name="subscriptions"),
]
