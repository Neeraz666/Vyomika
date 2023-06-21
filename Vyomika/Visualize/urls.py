from django.urls import path
from . import views

urlpatterns = [
    path('', views.createGraph, name='createGraph'),
    path('display/<int:snum>', views.displayGraph, name='displayGraph'),
]
