from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.management, name='management'),
    path('faculty/', views.faculty, name='faculty'),
    path('faculty/student/', views.studentMgmt, name = 'student'),
    path('faculty/student/addStudent/', views.addStudent, name = 'addStudent')
]