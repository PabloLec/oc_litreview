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
    path("get_modal_review", views.get_modal_review, name="get_modal_review"),
    path("get_modal_ticket_response", views.get_modal_ticket_response, name="get_modal_ticket_response"),
    path("ask_review", views.ask_review, name="ask_review"),
    path("ask_review/<ticket_instance>", views.ask_review, name="ask_review"),
    path("create_review", views.create_review, name="create_review"),
    path("reply_review", views.reply_review, name="reply_review"),
    path("delete_post/<post_type>/<post_id>", views.delete_post, name="delete_post"),
    path("posts", views.posts, name="posts"),
    path("sub", views.subscriptions, name="subscriptions"),
]
