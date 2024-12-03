from . import views as bulletin_views
from django.urls import path

urlpatterns = [
    path('',bulletin_views.home , name="home"),
    path('login/', bulletin_views.login_view, name='login'),
    path('logout/', bulletin_views.custom_logout, name='logout'),
    path('add_event/', bulletin_views.add_event, name='add_event'),
    path('calendar/', bulletin_views.calendar, name='calendar'),
    path('calendar.html/', bulletin_views.calendar, name='calendar_html'),
    path('placements/',bulletin_views.placement_list, name='placements'),
    path('habba/', bulletin_views.habba, name='habba'),
    path('sports/', bulletin_views.sports_view, name='sports'),
    path('technical/', bulletin_views.technical, name='technical'),
    path('cultural/', bulletin_views.cultural, name='cultural'),
    path('contact/', bulletin_views.contact, name='contact'),
    path('about/', bulletin_views.about, name='about'),
]