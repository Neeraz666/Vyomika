from django.urls import path
from . import views

urlpatterns = [
    path('', views.datainput, name='datainput'),
]
