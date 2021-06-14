from django.conf import settings
from website.models import Ticket, Review, UserFollows


def get_follows(user: settings.AUTH_USER_MODEL):
    """Get the users followed by given user.

    Args:
        user (settings.AUTH_USER_MODEL): User to be considered.

    Returns:
        list: Followed users.
    """

    user_follows = UserFollows.objects.filter(user=user.id)
    return list(user_follows)


def get_tickets(user: settings.AUTH_USER_MODEL):
    """Get tickets created by given user.

    Args:
        user (settings.AUTH_USER_MODEL): User to be considered.

    Returns:
        list: Tickets created by user.
    """

    tickets = Ticket.objects.filter(user=user.id)

    for ticket in tickets:
        ticket.type = "ticket"

    return list(tickets)


def get_reviews(user: settings.AUTH_USER_MODEL):
    """Get reviews created by given user.

    Args:
        user (settings.AUTH_USER_MODEL): User to be considered.

    Returns:
        list: Reviews created by user.
    """

    reviews = Review.objects.filter(user=user.id)

    for review in reviews:
        review.type = "review"

    return list(reviews)


def get_ticket_responses(ticket: Ticket):
    """Get reviews made in response to given ticket.

    Args:
        ticket (Ticket): Ticket to be considered.

    Returns:
        list: Reviews made in response to given ticket.
    """

    reviews = Review.objects.filter(ticket=ticket)

    for review in reviews:
        review.type = "review"

    return list(reviews)


def get_user_posts(user: settings.AUTH_USER_MODEL):
    """Get posts (Tickets and reviews) made by given user.

    Args:
        user (settings.AUTH_USER_MODEL): User to be considered.

    Returns:
        list: Posts created by user.
    """

    elements = get_tickets(user)
    elements += get_reviews(user)

    return sorted(elements, key=lambda x: x.time_created, reverse=True)


def generate_feed(user: settings.AUTH_USER_MODEL):
    """Generates full ticket and review feed, sorted by time created.

    Args:
        user (settings.AUTH_USER_MODEL):  User to be considered.

    Returns:
        list: Posts to be displayed in user feed.
    """

    follows = get_follows(user)

    elements = []
    for follow in follows:
        elements += get_tickets(follow.followed_user)
        elements += get_reviews(follow.followed_user)

    elements += get_user_posts(user)

    for ticket in get_tickets(user):
        elements += get_ticket_responses(ticket)

    return sorted(set(elements), key=lambda x: x.time_created, reverse=True)
