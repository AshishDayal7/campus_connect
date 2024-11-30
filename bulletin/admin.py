from django.contrib import admin
from .models import User, News, Placement,Room

admin.site.register(User)
admin.site.register(News)
admin.site.register(Room)
admin.site.register(Placement)
