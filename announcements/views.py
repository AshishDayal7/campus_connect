from django.shortcuts import render
from .models import Announcement
# Create your views here.


def a_home(request):
    context = {
        'announcements': Announcement.objects.all()
    }
    return render(request, 'announcements/a_home.html', context)

def a_profile(request):
    return render(request, 'announcements/a_profile.html')