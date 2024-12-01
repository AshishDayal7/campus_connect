from django.urls import path
from . import views 
urlpatterns=[
    path('',views.a_home,name='a-home'),
]