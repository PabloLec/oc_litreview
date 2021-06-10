from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.signup, name="signup"),
    path("is_username_available", views.is_username_available, name="is_username_available"),
    path("login", views.login_process, name="login"),
    path("logout", views.logout_process, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("posts", views.posts, name="posts"),
    path("sub", views.subscriptions, name="subscriptions"),
]
