from django.urls import path
from . import views 
urlpatterns=[
    path('',views.a_home,name='a_home'),
    path('profile/',views.a_profile,name='a_profile'),
]