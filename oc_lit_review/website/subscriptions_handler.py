from django.conf import settings
from website.models import UserFollows
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest


def handle_subscription_request(request: WSGIRequest, user: User):
    """Process subscription request and uses either add or delete follow.

    Args:
        request (WSGIRequest): POST request.
        user (User): User making the request.

    Returns:
        str: Success message to be displayed.
    """

    if request.POST.get("add"):
        return add_follow(request.POST.get("add"), user)
    elif request.POST.get("delete"):
        return delete_follow(request.POST.get("delete"), user)


def add_follow(to_add: str, user: User):
    """Adds a follow to given user.

    Args:
        to_add (str): Username to be added to follows.
        user (User): User to be considered.

    Returns:
        str: Success message to be displayed.
    """

    user_to_add = User.objects.get(username__iexact=to_add)
    follow = UserFollows(user=user, followed_user=user_to_add)
    follow.save()

    return f"Vous êtes désormais abonné à {user_to_add}."


def delete_follow(to_delete: str, user: User):
    """Removes a follow to given user.

    Args:
        to_delete (str): Username to be removed from follows.
        user (User): User to be considered.

    Returns:
        str: Success message to be displayed.
    """

    user_to_delete = User.objects.get(username__iexact=to_delete)
    follow = UserFollows.objects.get(user=user.id, followed_user=user_to_delete.id)
    follow.delete()

    return f"Vous êtes désabonné de {user_to_delete}."


def get_followers(user: User):
    """Get given users followers.

    Args:
        user (User): User to be considered.

    Returns:
        list: List of followers.
    """

    follows = UserFollows.objects.filter(followed_user=user)

    return [x.user for x in follows]
