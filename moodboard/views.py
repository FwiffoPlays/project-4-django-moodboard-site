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
    """
    Handles the creation of a new Moodboard.

    If the request method is POST, this function validates the submitted form,
    uploads images to Cloudinary, and creates a Moodboard object.
    If the request method is GET, this function renders a form to create a new
    Moodboard.
    """
    if request.method == "POST":
        form = MoodboardForm(request.POST)

        if form.is_valid():
            if request.FILES.getlist("image"):
                moodboard = form.save(commit=False)
                # Don't save the instance yet
                moodboard.user = (
                    request.user
                )  # Associate the logged-in user with the moodboard
                moodboard = form.save()  # Save the moodboard instance

                for img in request.FILES.getlist("image"):
                    uploaded_image = cloudinary.uploader.upload(img)
                    image_url = uploaded_image["secure_url"]
                    Image.objects.create(moodboard=moodboard, image=image_url)
                return redirect("moodboard:index")
            else:
                # Display an error to the user if no images are uploaded
                messages.error(request, "Please upload at least one image")
    else:
        form = MoodboardForm()

    context = {
        "form": form,
        # 'image_form': image_form,
    }

    return render(request, "moodboard/create_moodboard.html", context)


def edit_moodboard(request, moodboard_id):
    """
    Handles the editing of an existing Moodboard.

    If the user has permission to edit the Moodboard, this function allows
    them to modify the Moodboard's title, description, tags, and images.
    If the user does not have permission, a 403 Forbidden response is returned.
    """
    moodboard = get_object_or_404(Moodboard, pk=moodboard_id)

    if request.user == moodboard.user or request.user.is_staff:
        if request.method == "POST":
            form = MoodboardForm(request.POST, instance=moodboard)
            if form.is_valid():
                form.save()

                if request.FILES.getlist("image"):
                    # Delete existing images
                    Image.objects.filter(moodboard=moodboard).delete()

                    # Upload new images
                    for img in request.FILES.getlist("image"):
                        uploaded_image = cloudinary.uploader.upload(img)
                        image_url = uploaded_image["secure_url"]
                        Image.objects.create(moodboard=moodboard,
                                             image=image_url)

                messages.success(request, "Moodboard has been updated.")
                return redirect("moodboard:detail", pk=moodboard_id)
        else:
            form = MoodboardForm(instance=moodboard)
        images = Image.objects.filter(moodboard=moodboard)
        return render(
            request,
            "moodboard/edit_moodboard.html",
            {"form": form, "images": images, "moodboard": moodboard},
        )
    else:
        return HttpResponseForbidden(
            "You don't have permission to edit this Moodboard."
        )


@login_required
def delete_moodboard(request, pk):
    """
    Handles the deletion of a Moodboard.

    If the user has permission to delete the Moodboard, it is deleted and the
    user is redirected to the index page. If the user does not have
    permission, an error message is displayed.
    """
    moodboard = get_object_or_404(Moodboard, pk=pk)

    if request.user == moodboard.user or request.user.is_staff:
        moodboard.delete()
        messages.success(request, "Moodboard has been deleted.")
        return redirect("moodboard:index")
    else:
        messages.error(request, "You do not have permission to delete this "
                                "moodboard.")
        return redirect("moodboard:detail", pk=pk)


def get_queryset(request):
    """
    Returns a queryset of Moodboard objects based on the search query.

    If there is a search query, this function filters Moodboard objects by
    title, description, or tags containing the query. If there is no
    search query, it returns all Moodboard objects.
    """
    query = request.GET.get("q")
    if query:
        moodboards = Moodboard.objects.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(tags__icontains=query)
        )
    else:
        moodboards = Moodboard.objects.all()
    return moodboards


def index(request):
    """
    Displays a list of all Moodboard objects or a filtered list based on the
    search query.
    """
    moodboards = get_queryset(request)
    return render(request, "moodboard/index.html", {"moodboards": moodboards})


def detail(request, pk):
    """
    Displays the details of a Moodboard, including its title, description,
    tags, and images.
    """
    moodboard = Moodboard.objects.get(pk=pk)
    images = Image.objects.filter(moodboard_id=pk)
    context = {"moodboard": moodboard, "images": images}
    return render(request, "moodboard/detail.html", context)
