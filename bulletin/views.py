# bulletin/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib import messages
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Placement, Room, Message, Event

def home(request):
    return render(request, 'bulletin/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'bulletin/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'bulletin/login.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('home')  # Redirect to home page after logout


def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'bulletin/rooms.html', {"rooms": rooms})

def room(request, slug):
    room_name = Room.objects.get(slug=slug).name
    messages = Message.objects.filter(room=Room.objects.get(slug=slug))
    return render(request, 'bulletin/room.html', {"room_name": room_name, "slug": slug, 'messages': messages})

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
    placements = Placement.objects.all().values('company_name', 'job_title', 'description', 'created_at', 'updated_at')
    context = {
        'placements': list(placements)
    }
    return render(request, 'bulletin/placement.html', context)


'''# main/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib import messages
from .forms import SignupForm
from .models import Placement,Room,Message
from django.contrib.auth import logout


def rooms(request):
    rooms=Room.objects.all()
    return render(request, "rooms.html",{"rooms":rooms})

def room(request,slug):
    room_name=Room.objects.get(slug=slug).name
    messages=Message.objects.filter(room=Room.objects.get(slug=slug))
    
    return render(request, "room.html",{"room_name":room_name,"slug":slug,'messages':messages})

def home(request):
    return render(request, 'bulletin/home.html')

def calendar(request):
    return render(request, 'calendar.html')




def add_event(request):
    if request.method == 'POST':
        title = request.POST.get('eventTitle')
        start = request.POST.get('eventStart')
        end = request.POST.get('eventEnd')
        Event.objects.create(title=title, start=start, end=end)
        return redirect('calendar')

    return render(request, 'add_event.html')

def events_data(request):
    events = Event.objects.all().values('title', 'start', 'end')
    events_list = list(events)
    return JsonResponse(events_list, safe=False)




def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            # Redirect to a success page or home page
            return redirect('home')  # Replace 'home' with your desired URL name
        else:
            # Return an invalid login error message
            messages.error(request, 'Invalid username or password.')
    
    # Render the login page with any error messages
    return render(request, 'login.html')


# collegebulletin/miniproject/views.py



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# views.py in your Django app



# def placement_list(request):
#     placements = Placement.objects.all()
#     data = list(placements.values('company_name', 'job_title', 'description', 'created_at', 'updated_at'))
#     return JsonResponse(data, safe=False)

def placement_list(request):
    placements = Placement.objects.all().values('company_name', 'job_title', 'description', 'created_at', 'updated_at')
    context = {
        'placements': list(placements)
    }
    return render(request, 'placement.html', context)

def custom_logout(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/home/')


# from django.shortcuts import render

# def home(request):
#     return render(request, 'home.html')

# def add_event(request):
#     return render(request, 'add_event.html')

# def calendar(request):
#     return render(request, 'calendar.html')
'''