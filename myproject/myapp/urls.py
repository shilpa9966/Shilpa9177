from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('mca101/',views.mca101, name='mca101'),
    path('mca102/',views.mca102, name='mca102'),
    path('mca103/',views.mca103, name='mca103'),
]
# Create your views here.
