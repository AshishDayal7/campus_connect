# campus_connect/urls.py
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bulletin.urls')),
    path('announcements/',include('announcements.urls')),
    path('accounts/',include('allauth.urls')),
]