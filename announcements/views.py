from django.shortcuts import render, redirect
from .models import Announcement
from .forms import ProfileUpdateForm 
from django.contrib import messages
# Create your views here.


def a_home(request):
    context = {
        'announcements': Announcement.objects.all()
    }
    return render(request, 'announcements/a_home.html', context)

from django.shortcuts import render
from .forms import ProfileUpdateForm
from django.contrib.auth.decorators import login_required

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
