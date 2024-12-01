from . import views as bulletin_views
from django.urls import path

urlpatterns = [
    path('login/', bulletin_views.login_view, name='login'),
    path('logout/', bulletin_views.custom_logout, name='custom_logout'),
    path('add_event/', bulletin_views.add_event, name='add_event'),
    path('calendar/', bulletin_views.calendar, name='calendar'),
    path('calendar.html/', bulletin_views.calendar, name='calendar_html'),
    path('placements/',bulletin_views.placements, name='placements')
]