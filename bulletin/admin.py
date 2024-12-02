from django.contrib import admin
from .models import User, News, Placement
from .models import Sport, Fixture, Result

admin.site.register(User)
admin.site.register(News)
admin.site.register(Placement)
admin.site.register(Sport)
admin.site.register(Fixture)
admin.site.register(Result)
