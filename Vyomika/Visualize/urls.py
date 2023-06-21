from django.urls import path
from . import views

urlpatterns = [
    path('', views.createGraph, name='createGraph'),
    path('display', views.displayGraph, name='displayGraph'),
]
