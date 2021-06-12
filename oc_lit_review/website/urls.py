from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.signup, name="signup"),
    path("is_username_available", views.is_username_available, name="is_username_available"),
    path("login", views.login_process, name="login"),
    path("logout", views.logout_process, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("get_modal_ticket", views.get_modal_ticket, name="get_modal_ticket"),
    path("get_modal_ticket/<ticket_instance>", views.get_modal_ticket, name="get_modal_ticket"),
    path("get_modal_full_review", views.get_modal_full_review, name="get_modal_full_review"),
    path("get_modal_simple_review", views.get_modal_simple_review, name="get_modal_simple_review"),
    path("get_modal_simple_review/<review_instance>", views.get_modal_simple_review, name="get_modal_simple_review"),
    path("make_ticket", views.make_ticket, name="make_ticket"),
    path("make_ticket/<ticket_instance>", views.make_ticket, name="make_ticket"),
    path("make_full_review", views.make_full_review, name="make_full_review"),
    path("make_simple_review", views.make_simple_review, name="make_simple_review"),
    path("make_simple_review/<review_instance>", views.make_simple_review, name="make_simple_review"),
    path("delete_post/<post_type>/<post_id>", views.delete_post, name="delete_post"),
    path("posts", views.posts, name="posts"),
    path("sub", views.subscriptions, name="subscriptions"),
]
