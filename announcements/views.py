from django.shortcuts import render, redirect
from .models import Announcement
from .forms import ProfileUpdateForm,AnnouncementForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError

@login_required
def create_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.author = request.user
            try:
                announcement.full_clean()
                announcement.save()
                messages.success(request, 'Announcement created successfully!')
                return redirect('a_home')
            except ValidationError as e:
                messages.error(request, e.message)
                return render(request, 'a_home.html', {'form': form})
    else:
        form = AnnouncementForm()
    return render(request, 'your_template.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, 
                                 request.FILES, 
                                 instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
        messages.success(request, f'Your account has been updated!')
        return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form
    }
    return render(request, 'announcements/profile.html', context)

def a_home(request):
    context = {
        'announcements': Announcement.objects.all()
    }
    return render(request, 'announcements/a_home.html', context)
