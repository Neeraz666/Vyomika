from django.urls import path
from . import views

urlpatterns = [
    path('', views.management, name='management'),
    path('faculty/', views.faculty, name='faculty'),
    path('student/', views.studentMgmt, name = 'student')
]
