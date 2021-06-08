from django.contrib import admin

from .models import *

admin.site.register(Ticket)
admin.site.register(Review)
admin.site.register(UserFollows)
admin.site.register(Profile)
