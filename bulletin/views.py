# bulletin/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .models import Placement, Event  #removed room n messages- chats
from .models import Sport, Fixture, Result


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

def placement_list(request):
    placements = Placement.objects.all()
    return render(request, 'bulletin/placement.html', {'placements': placements})

def habba(request):
    return render(request, 'bulletin/habba.html')

def sports_view(request):
    sports = Sport.objects.all()
    selected_sport = request.GET.get('sport')
    fixtures = Fixture.objects.filter(sport__name=selected_sport) if selected_sport else []
    results = Result.objects.filter(fixture__sport__name=selected_sport) if selected_sport else []
    
    return render(request, 'bulletin/sports.html', {
        'sports': sports,
        'fixtures': fixtures,
        'results': results,
        'selected_sport': selected_sport,
        
    })

    
def technical(request):
    return render(request, 'bulletin/technical.html')

def cultural(request):
    return render(request, 'bulletin/cultural.html')

def contact(request):
    return render(request, 'bulletin/contact.html')

def about(request):
    return render(request, 'bulletin/about.html')