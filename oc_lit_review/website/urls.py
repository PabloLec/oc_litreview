from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.signup, name="signup"),
    path("is_username_available", views.is_username_available, name="is_username_available"),
    path("login", views.login_process, name="login"),
    path("logout", views.logout_process, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("ask_review", views.ask_review, name="ask_review"),
    path("create_review", views.create_review, name="create_review"),
    path("posts", views.posts, name="posts"),
    path("sub", views.subscriptions, name="subscriptions"),
]
