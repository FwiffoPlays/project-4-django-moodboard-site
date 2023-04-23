from django.urls import path, include
from . import views

app_name = 'moodboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.detail, name='detail'),
    path('create/', views.create_moodboard, name='create_moodboard'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('edit/<int:moodboard_id>/', views.edit_moodboard, name='edit_moodboard'),
    path('delete/<int:pk>/', views.delete_moodboard, name='delete_moodboard'),
]