from django import forms
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'image']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }