from django.shortcuts import render, redirect
from .models import Announcement
from .forms import ProfileUpdateForm,AnnouncementForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

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


class AnnouncementListView(ListView):
    model=Announcement
    template_name= 'announcements/a_home.html'
    context_object_name='announcements'
    ordering=['-date_posted']

class AnnouncementDetailView(DetailView):
    model=Announcement
    #template naming convention = <app>/<model>_<viewtype>.html=== announcement_detail.html

class AnnouncementCreateView(LoginRequiredMixin, CreateView):
    model = Announcement
    fields = ['title', 'content']
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if form.instance:
            form.instance.author = self.request.user
        return form

    def form_valid(self, form):
        # Set author again to be safe
        form.instance.author = self.request.user
        try:
            # Let form handle validation and saving
            return super().form_valid(form)
        except ValidationError as e:
            messages.error(self.request, str(e))
            return self.form_invalid(form)

'''we can use decorators on CBV so we use mixin - only those who have logged in otherwise redirect them to login '''
class AnnouncementUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model=Announcement
    fields=['title','content']
    #even update is here - <modelname>_form.html

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        announcement=self.get_object()
        if self.request.user == announcement.author:
            return True
        return False

class AnnouncementDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Announcement
    success_url="/"
    #template it expects , is asking if we are sure we want to delete - where it'll convert get request into post request 
    #<model>_confirm_delete
    def test_func(self):
        announcement=self.get_object()
        if self.request.user == announcement.author:
            return True
        return False