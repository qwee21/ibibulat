from django.contrib import admin

from users.models import Performer, Buyer, User

admin.site.register(Performer)
admin.site.register(Buyer)
admin.site.register(User)