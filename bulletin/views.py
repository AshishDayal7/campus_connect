# bulletin/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .models import Placements, Event #removed room n messages 

def home(request):
    return render(request, 'bulletin/index.html')

def login_view(request):
    return render(request, 'bulletin/login.html')


def custom_logout(request):
    logout(request)
    return redirect('home')  # Redirect to home page after logout

def add_event(request):
    if request.method == 'POST':
        title = request.POST.get('eventTitle')
        start = request.POST.get('eventStart')
        end = request.POST.get('eventEnd')
        Event.objects.create(title=title, start=start, end=end)
        return redirect('calendar')

    return render(request, 'bulletin/add_event.html')

def events_data(request):
    events = Event.objects.all().values('title', 'start', 'end')
    events_list = list(events)
    return JsonResponse(events_list, safe=False)

def calendar(request):
    return render(request, 'bulletin/calendar.html')

def placements(request):
    placements = Placements.objects.all().values('company_name', 'job_title', 'description', 'created_at', 'updated_at')
    context = {
        'placements': list(placements)
    }
    return render(request, 'bulletin/placement.html', context)
