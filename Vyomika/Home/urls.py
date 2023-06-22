from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='displaygraph'),
    path('about/', views.about, name='about'),
    path('contact/', views.contactUs, name='contact')
]
