from django.conf import settings
from website.models import UserFollows
from django.contrib.auth.models import User


def handle_subscription_request(request, user):
    if request.POST.get("add"):
        return add_follow(request.POST.get("add"), user)
    elif request.POST.get("delete"):
        return delete_follow(request.POST.get("delete"), user)


def add_follow(to_add, user):
    user_to_add = User.objects.get(username__iexact=to_add)
    follow = UserFollows(user=user, followed_user=user_to_add)
    follow.save()

    return f"Vous êtes désormais abonné à {user_to_add}."


def delete_follow(to_delete, user):
    user_to_delete = User.objects.get(username__iexact=to_delete)
    follow = UserFollows.objects.get(user=user.id, followed_user=user_to_delete.id)
    follow.delete()

    return f"Vous êtes désabonné de {user_to_delete}."


def get_followers(user):
    follows = UserFollows.objects.filter(followed_user=user)

    return [x.user for x in follows]
