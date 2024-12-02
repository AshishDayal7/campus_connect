from django.urls import path
from . import views 
from .views import (AnnouncementListView,
                    AnnouncementDetailView,
                    AnnouncementCreateView,
                    AnnouncementUpdateView,
                    AnnouncementDeleteView)
urlpatterns=[
    path('',AnnouncementListView.as_view(),name='a_home'),
    path('profile/',views.profile,name='profile'),
    path('<int:pk>/',AnnouncementDetailView.as_view(),name='announcement-detail'),
    path('new/',AnnouncementCreateView.as_view(),name='announcement-create'),
    path('<int:pk>/update/',AnnouncementUpdateView.as_view(),name='announcement-update'),
    path('<int:pk>/delete/',AnnouncementDeleteView.as_view(),name='announcement-delete'),
]