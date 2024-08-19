from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.members, name='members'),
    path('blogs/', views.members, name='profile'),
]