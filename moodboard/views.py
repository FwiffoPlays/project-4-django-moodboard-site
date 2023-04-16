from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import MoodboardForm, ImageFormSet
from .models import Moodboard, Image

def create_moodboard(request):
    if request.method == 'POST':
        form = MoodboardForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, prefix='image_form')

        if form.is_valid() and formset.is_valid():
            moodboard = form.save(commit=False)  # Don't save the instance yet
            moodboard.user = request.user  # Associate the logged-in user with the moodboard
            moodboard = form.save() # Save the moodboard instance
            for inline_form in formset:
                if inline_form.cleaned_data:
                    image = inline_form.save(commit=False)
                    image.moodboard = moodboard
                    image.save()

            return redirect('moodboard:index') 

    else:
        form = MoodboardForm()
        formset = ImageFormSet(prefix='image_form')

    context = {
        'form': form,
        'formset': formset,
    }

    return render(request, 'create_moodboard.html', context)

def index(request):
    moodboards = Moodboard.objects.all()
    return render(request, 'index.html', {'moodboards': moodboards})

def detail(request, pk):
    moodboard = Moodboard.objects.get(pk=pk)
    images = Image.objects.filter(moodboard_id=pk)
    context = {
        'moodboard': moodboard,
        'images': images
    }
    return render(request, 'detail.html', context)
