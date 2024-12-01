# campus_connect/urls.py
from django.contrib import admin
from django.urls import path,include
from bulletin import views as bulletin_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bulletin_views.home, name="home"),
    path('accounts/',include('allauth.urls')),
    path('login/', bulletin_views.login_view, name='login'),
    path('logout/', bulletin_views.custom_logout, name='custom_logout'),
    path("home/chat/", bulletin_views.rooms, name="rooms"),
    path('home/add_event/', bulletin_views.add_event, name='add_event'),
    path('calendar/', bulletin_views.calendar, name='calendar'),
    path('calendar.html/', bulletin_views.calendar, name='calendar_html'),
]