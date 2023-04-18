from django.shortcuts import render, redirect, get_object_or_404
import cloudinary.uploader
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MoodboardForm, ImageForm
from .models import Moodboard, Image

def create_moodboard(request):
    if request.method == 'POST':
        form = MoodboardForm(request.POST)
        #image_form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            if request.FILES.getlist('image'):
                moodboard = form.save(commit=False)  # Don't save the instance yet
                moodboard.user = request.user  # Associate the logged-in user with the moodboard
                moodboard = form.save() # Save the moodboard instance
                
                for img in request.FILES.getlist('image'):
                    uploaded_image = cloudinary.uploader.upload(img)
                    image_url = uploaded_image['secure_url']
                    Image.objects.create(moodboard=moodboard, image=image_url)
                return redirect('moodboard:index') 
            else:
                #Display an error to the user if no images are uploaded
                messages.error(request, 'Please upload at least one image')
    else:
        form = MoodboardForm()
        #image_form = ImageForm(prefix='image_form')

    context = {
        'form': form,
        #'image_form': image_form,
    }

    return render(request, 'moodboard/create_moodboard.html', context)

@login_required
def delete_moodboard(request, pk):
    moodboard = get_object_or_404(Moodboard, pk=pk)
    
    if request.user == moodboard.user or request.user.is_staff:
        moodboard.delete()
        messages.success(request, 'Moodboard has been deleted.')
        return redirect('moodboard:index')
    else:
        messages.error(request, 'You do not have permission to delete this moodboard.')
        return redirect('moodboard:detail', pk=pk)

def index(request):
    moodboards = Moodboard.objects.all()
    return render(request, 'moodboard/index.html', {'moodboards': moodboards})

def detail(request, pk):
    moodboard = Moodboard.objects.get(pk=pk)
    images = Image.objects.filter(moodboard_id=pk)
    context = {
        'moodboard': moodboard,
        'images': images
    }
    return render(request, 'moodboard/detail.html', context)
