from django.shortcuts import render, redirect
from .forms import MoodboardForm, ImageFormSet
from .models import Moodboard

def create_moodboard(request):
    if request.method == 'POST':
        form = MoodboardForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, prefix='image_form')

        if form.is_valid() and formset.is_valid():
            moodboard = form.save()
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

    return render(request, 'moodboard/create_moodboard.html', context)

def index(request):
    moodboards = Moodboard.objects.all()
    return render(request, 'moodboard/index.html', {'moodboard': moodboards})

def detail(request, moodboard_id):
    moodboard = Moodboard.objects.get(pk=moodboard_id)
    return render(request, 'moodboard/detail.html', {'moodboard': moodboard})
