from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Moodboard(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.CharField(max_length=500, blank=True)

    def tags_as_list(self):
        return self.tags.split(',')
        
    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='moodboard_images')
    moodboard = models.ForeignKey(Moodboard, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk}"

    
