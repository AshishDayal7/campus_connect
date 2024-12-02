from django import forms
from .models import Profile
from .models import Announcement

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'image']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }