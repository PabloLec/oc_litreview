from django.conf import settings

from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import CharField, Value
from django.contrib.auth.models import User
from website.feed_generator import *
from website.subscriptions_handler import *
from django.contrib.auth.decorators import login_required


def index(request):

    return render(request, "index.html")


def login_process(request):
    if request.method != "POST":
        return redirect('index')

    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('dashboard')
    else:
        messages.error(request, "Nom d'utilisateur et/ou mot de passe invalide.")
        return redirect('index')

def logout_process(request):
    logout(request)
    return redirect('index')

@login_required(login_url='/')
def dashboard(request):
    feed = generate_feed(request.user)

    return render(request, "dashboard.html", context={"feed": feed})

@login_required(login_url='/')
def posts(request):

    posts = generate_user_posts(request.user)

    return render(request, "posts.html", context={"posts": posts})

@login_required(login_url='/')
def subscriptions(request):

    if request.method == "POST":
        messages.info(request, handle_request(request, request.user))

    follows = get_follows(request.user)
    followed_users = [x.followed_user for x in follows]

    available_users = [x for x in User.objects.all() if x not in followed_users+[request.user]]

    return render(request, "subscriptions.html", context={"subs": followed_users, "users": available_users})
