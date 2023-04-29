from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Moodboard(models.Model):
    """
    Represents a Moodboard, containing a title, description, associated user,
    and tags.

    Attributes:
        title (CharField): The title of the Moodboard.
        description (TextField): A description of the Moodboard (optional).
        user (ForeignKey): A foreign key to the User who created the Moodboard.
        tags (CharField): A comma-separated list of tags associated with the
        Moodboard (optional).
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.CharField(max_length=500, blank=True)

    def tags_as_list(self):
        """
        Returns the tags as a list of strings.

        Returns:
            list: A list of tags as strings.
        """
        return self.tags.split(",")

    def __str__(self):
        """
        Returns a string representation of the Moodboard object.

        Returns:
            str: The title of the Moodboard.
        """
        return self.title


class Image(models.Model):
    """
    Represents an image associated with a Moodboard.

    Attributes:
        image (ImageField): The image file.
        moodboard (ForeignKey): A foreign key to the Moodboard to which the
        image belongs.
    """
    image = models.ImageField(upload_to="moodboard_images")
    moodboard = models.ForeignKey(
        Moodboard, related_name="images", on_delete=models.CASCADE
    )

    def __str__(self):
        """
        Returns a string representation of the Image object.

        Returns:
            str: The primary key of the Image object.
        """
        return f"{self.pk}"
