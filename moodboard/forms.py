from django import forms
from .models import Moodboard, Image

class MoodboardForm(forms.ModelForm):
    class Meta:
        model = Moodboard
        fields = ['title', 'description', 'tags']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
        }
