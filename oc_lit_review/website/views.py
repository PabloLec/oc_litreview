from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest

from website.feed_generator import *
from website.subscriptions_handler import *
from website.forms import *
from website.models import *


def index(request: WSGIRequest):
    """Landing page view.

    Args:
        request (WSGIRequest): Received request.

    Returns:
        HttpResponseRedirect: Request response.
    """

    if request.user.is_authenticated:
        return redirect("dashboard")

    register_form = RegisterForm()

    return render(request, "index.html", context={"register_form": register_form})


def signup(request: WSGIRequest):
    """Handles user registration request.

    Args:
        request (WSGIRequest): Received request.

    Returns:
        HttpResponseRedirect: Request response.
    """

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.info(request, "Bienvenue sur LIT Review!")
            return redirect("dashboard")

    messages.error(request, "Une erreur s'est produite lors de votre inscription.")
    return redirect("index")


def is_username_available(request: WSGIRequest):
    """Checks if given username is not yet taken in existing database.

    Args:
        request (WSGIRequest): Received request.

    Returns:
        HttpResponse: Either true or false.
    """

    if request.method == "POST":
        all_usernames = [x.username.lower() for x in User.objects.all()]
        if request.POST["username"].lower() in all_usernames:
            return HttpResponse("false")
        else:
            return HttpResponse("true")


def login_process(request: WSGIRequest):
    """Handles user login and arguments validation.

    Args:
        request (WSGIRequest): Received request.

    Returns:
        HttpResponseRedirect: Request response.
    """

    if request.method != "POST":
        return redirect("index")

    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect("dashboard")
    else:
        messages.error(request, "Nom d'utilisateur et/ou mot de passe invalide.")
        return redirect("index")


def logout_process(request: WSGIRequest):
    """Handles user logout process.

    Args:
        request (WSGIRequest): Received request.

    Returns:
        HttpResponseRedirect: Request response.
    """

    logout(request)
    return redirect("index")


@login_required(login_url="/")
def dashboard(request: WSGIRequest):
    """Logged user main page, displays posts feed.

    Args:
        request (WSGIRequest): Received request.

    Returns:
        HttpResponseRedirect: Request response.
    """

    feed = generate_feed(request.user)
    return render(
        request,
        "dashboard.html",
        context={"feed": feed},
    )


@login_required(login_url="/")
def make_ticket(request: WSGIRequest, ticket_instance: Ticket = None):
    """Handles ticket creation request.

    Args:
        request (WSGIRequest): Received request.
        ticket_instance (Ticket, optional): If ticket edit, ticket id to be considered. Defaults to None.

    Returns:
        HttpResponseRedirect: Request response.
    """

    if request.method == "POST":
        if ticket_instance:
            ticket_instance = Ticket.objects.get(pk=ticket_instance)
            if ticket_instance.user != request.user:
                messages.error(request, "Une erreur s'est produite lors de votre publication.")
                return redirect("dashboard")

        form = AskReviewForm(request.POST, request.FILES, prefix="ask", instance=ticket_instance)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            messages.info(request, "Votre ticket vient d'être publié!")
            return redirect("dashboard")

    messages.error(request, "Une erreur s'est produite lors de votre publication.")
    return redirect("dashboard")


@login_required(login_url="/")
def make_full_review(request: WSGIRequest):
    """Handles full (ticket + proper review) review creation.

    Args:
        request (WSGIRequest): Received request.

    Returns:
        HttpResponseRedirect: Request response.
    """

    if request.method == "POST":
        form_ask = AskReviewForm(request.POST, request.FILES, prefix="ask")
        form_create = CreateReviewForm(request.POST, prefix="create")
        if form_ask.is_valid() and form_create.is_valid():
            ticket = form_ask.save(commit=False)
            ticket.user = request.user
            ticket.save()

            review = form_create.save(commit=False)
            review.user = request.user
            review.ticket = Ticket.objects.get(pk=ticket.pk)
            review.save()

            messages.info(request, "Votre critique vient d'être publiée!")
            return redirect("dashboard")

    messages.error(request, "Une erreur s'est produite lors de votre publication.")
    return redirect("dashboard")


@login_required(login_url="/")
def make_simple_review(request: WSGIRequest, review_instance: Review = None):
    """Handles simple (response to a ticket) review creation.

    Args:
        request (WSGIRequest): Received request.
        review_instance (Review, optional): If review edit, review id to be considered. Defaults to None.

    Returns:
        HttpResponseRedirect: Request response.
    """

    if request.method == "POST":
        if review_instance:
            review_instance = Review.objects.get(pk=review_instance)
            if review_instance.user != request.user:
                messages.error(request, "Une erreur s'est produite lors de votre publication.")
                return redirect("dashboard")

        form = CreateReviewForm(request.POST, prefix="create", instance=review_instance)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            if not review_instance:
                review.ticket = Ticket.objects.get(pk=request.POST["ticket-id"])
            review.save()

            messages.info(request, "Votre critique vient d'être publiée!")
            return redirect("dashboard")

    messages.error(request, "Une erreur s'est produite lors de votre publication.")
    return redirect("dashboard")


@login_required(login_url="/")
def delete_post(request: WSGIRequest, post_type: str, post_id: str):
    """Handles post deletion.

    Args:
        request (WSGIRequest): Received request.
        post_type (str): Post type (either "ticket" or "review").
        post_id (str): Post unique id to be considered.

    Returns:
        HttpResponseRedirect: Request response.
    """

    if request.method == "POST":
        if post_type == "ticket":
            object_to_delete = Ticket.objects.get(pk=post_id)
        elif post_type == "review":
            object_to_delete = Review.objects.get(pk=post_id)

        if object_to_delete.user != request.user:
            messages.error(request, "Une erreur s'est produite lors de la suppression.")
            return redirect("dashboard")

        object_to_delete.delete()
        messages.info(request, "Votre publication a été supprimée.")
        return redirect("dashboard")

    messages.error(request, "Une erreur s'est produite lors de la suppression.")
    return redirect("dashboard")


@login_required(login_url="/")
def posts(request: WSGIRequest):
    """User own posts view.

    Args:
        request (WSGIRequest): Received request.

    Returns:
        HttpResponseRedirect: Request response.
    """

    posts = get_user_posts(request.user)

    return render(request, "posts.html", context={"posts": posts})


@login_required(login_url="/")
def subscriptions(request: WSGIRequest):
    """User follows/followers view.

    Args:
        request (WSGIRequest): Received request.

    Returns:
        HttpResponseRedirect: Request response.
    """

    if request.method == "POST":

        messages.info(request, handle_subscription_request(request, request.user))

    follows = get_follows(request.user)
    followed_users = [x.followed_user for x in follows]
    followers = get_followers(request.user)

    available_users = [x for x in User.objects.all() if x not in followed_users + [request.user]]

    return render(
        request,
        "subscriptions.html",
        context={"follows": followed_users, "followers": followers, "users": available_users},
    )


@login_required(login_url="/")
def get_modal_ticket(request: WSGIRequest, ticket_instance: Ticket = None):
    """Gets ticket creation/edit modal HTML code.

    Args:
        request (WSGIRequest): Received request.
        ticket_instance (Ticket, optional): If ticket edit, ticket id to be considered. Defaults to None. Defaults to None.

    Returns:
        HttpResponseRedirect: Request response.
    """

    if ticket_instance:
        ticket_instance = Ticket.objects.get(pk=ticket_instance)
    make_ticket_form = AskReviewForm(prefix="ask", instance=ticket_instance)

    return render(
        request,
        "components/modal_ticket.html",
        context={
            "make_ticket_form": make_ticket_form,
        },
    )


@login_required(login_url="/")
def get_modal_full_review(request: WSGIRequest):
    """Gets full (ticket + proper review) review creation modal.

    Args:
        request (WSGIRequest): Received request.

    Returns:
        HttpResponseRedirect: Request response.
    """

    make_full_review_form = CreateReviewForm(prefix="create")
    make_ticket_form = AskReviewForm(prefix="ask")

    return render(
        request,
        "components/modal_full_review.html",
        context={"make_ticket_form": make_ticket_form, "make_full_review_form": make_full_review_form},
    )


@login_required(login_url="/")
def get_modal_simple_review(request: WSGIRequest, review_instance: Review = None):
    """Gets simple (response to a ticket) review creation modal.

    Args:
        request (WSGIRequest): Received request.
        review_instance (Review, optional): If review edit, review id to be considered. Defaults to None. Defaults to None. Defaults to None.

    Returns:
        HttpResponseRedirect: Request response.
    """

    if review_instance:
        review_instance = Review.objects.get(pk=review_instance)
    make_full_review_form = CreateReviewForm(prefix="create", instance=review_instance)

    return render(
        request,
        "components/modal_simple_review.html",
        context={
            "make_full_review_form": make_full_review_form,
        },
    )
