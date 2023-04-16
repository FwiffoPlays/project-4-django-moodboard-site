from django.urls import path
from . import views

app_name = 'moodboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_moodboard, name='create_moodboard'),
]