from django.conf import settings
from website.models import Ticket, Review, UserFollows


def get_follows(user):
    user_follows = UserFollows.objects.filter(user=user.id)
    return list(user_follows)


def get_tickets(user):
    tickets = Ticket.objects.filter(user=user.id)

    for ticket in tickets:
        ticket.type = "ticket"

    return list(tickets)


def get_reviews(user):
    reviews = Review.objects.filter(user=user.id)

    for review in reviews:
        review.type = "review"

    return list(reviews)


def generate_feed(user):
    follows = get_follows(user)

    elements = []
    for follow in follows:
        elements += get_tickets(follow.followed_user)
        elements += get_reviews(follow.followed_user)

    elements += generate_user_posts(user)

    for ticket in get_tickets(user):
        elements += get_ticket_responses(ticket)

    return sorted(elements, key=lambda x: x.time_created, reverse=True)

def get_ticket_responses(ticket):
    reviews = Review.objects.filter(ticket=ticket)

    for review in reviews:
        review.type = "review"

    return list(reviews)

def generate_user_posts(user):
    elements = get_tickets(user)
    elements += get_reviews(user)

    return sorted(elements, key=lambda x: x.time_created, reverse=True)
