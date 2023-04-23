from django.shortcuts import render, redirect, get_object_or_404
import cloudinary.uploader
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MoodboardForm, ImageForm
from .models import Moodboard, Image


def create_moodboard(request):
    if request.method == 'POST':
        form = MoodboardForm(request.POST)

        if form.is_valid():
            if request.FILES.getlist('image'):
                moodboard = form.save(commit=False)  # Don't save the instance yet
                moodboard.user = request.user  # Associate the logged-in user with the moodboard
                moodboard = form.save()  # Save the moodboard instance
                
                for img in request.FILES.getlist('image'):
                    uploaded_image = cloudinary.uploader.upload(img)
                    image_url = uploaded_image['secure_url']
                    Image.objects.create(moodboard=moodboard, image=image_url)
                return redirect('moodboard:index') 
            else:
                # Display an error to the user if no images are uploaded
                messages.error(request, 'Please upload at least one image')
    else:
        form = MoodboardForm()

    context = {
        'form': form,
        # 'image_form': image_form,
    }

    return render(request, 'moodboard/create_moodboard.html', context)


def edit_moodboard(request, moodboard_id):
    moodboard = get_object_or_404(Moodboard, pk=moodboard_id)

    if request.user == moodboard.user or request.user.is_staff:
        if request.method == 'POST':
            form = MoodboardForm(request.POST, instance=moodboard)
            if form.is_valid():
                form.save()

                # Delete existing images
                Image.objects.filter(moodboard=moodboard).delete()

                # Upload new images
                for img in request.FILES.getlist('image'):
                    uploaded_image = cloudinary.uploader.upload(img)
                    image_url = uploaded_image['secure_url']
                    Image.objects.create(moodboard=moodboard, image=image_url)

                messages.success(request, 'Moodboard has been updated.')
                return redirect('moodboard:detail', pk=moodboard_id)
        else:
            form = MoodboardForm(instance=moodboard)
        images = Image.objects.filter(moodboard=moodboard)
        return render(request, 'moodboard/edit_moodboard.html', {'form': form, 'images': images, 'moodboard': moodboard})
    else:
        return HttpResponseForbidden("You don't have permission to edit this Moodboard.")

@login_required
def delete_moodboard(request, pk):
    moodboard = get_object_or_404(Moodboard, pk=moodboard_is)
    
    if request.user == moodboard.user or request.user.is_staff:
        moodboard.delete()
        messages.success(request, 'Moodboard has been deleted.')
        return redirect('moodboard:index')
    else:
        messages.error(request, 'You do not have permission to delete this moodboard.')
        return redirect('moodboard:detail', pk=moodboard_id)


def get_queryset(request):
    query = request.GET.get('q')
    if query:
        moodboards = Moodboard.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(tags__icontains=query)
        )
    else:
        moodboards = Moodboard.objects.all()
    return moodboards


def index(request):
    moodboards = get_queryset(request)
    return render(request, 'moodboard/index.html', {'moodboards': moodboards})


def detail(request, pk):
    moodboard = Moodboard.objects.get(pk=pk)
    images = Image.objects.filter(moodboard_id=pk)
    context = {
        'moodboard': moodboard,
        'images': images
    }
    return render(request, 'moodboard/detail.html', context)


