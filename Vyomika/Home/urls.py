from django.urls import path
from . import views

urlpatterns = [
    path('', views.displaygraph, name='displaygraph'),
    path('about/', views.about, name='about')
]
