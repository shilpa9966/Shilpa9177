from django.urls import path
from . import views
urlpatterns = [
     path('displaygreen/', views.displaygreen,name='displaygreen'),
     path('displaygreen2/', views.displaygreen2,name='displaygreen2'),
]

