from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.createGraph, name='dataInput'),
    path('display/<int:snum>', views.displayGraph, name='displayGraph')
]
