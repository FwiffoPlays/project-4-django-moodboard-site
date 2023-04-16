from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Moodboard(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    image = CloudinaryField('moodboard_images')
    moodboard = models.ForeignKey(Moodboard, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.moodboard.title} - Image {self.id}"
