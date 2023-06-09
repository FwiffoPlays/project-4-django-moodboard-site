# Generated by Django 3.2.18 on 2023-04-16 19:56

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moodboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.RemoveField(
            model_name='moodboard',
            name='tags',
        ),
        migrations.AddField(
            model_name='moodboard',
            name='tags',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
