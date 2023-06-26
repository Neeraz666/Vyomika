from django.urls import path
from . import views

urlpatterns = [
    path('', views.management, name='management'),
    path('faculty/', views.faculty, name='faculty'),
    path('faculty/bsitstudents/', views.bsit, name = 'bsitstudent'),
    path('faculty/bbastudents/', views.bba, name = 'bbastudent'),
    path('faculty/<str:stdfaculty>/addStudent/', views.addStudent, name = 'addStudent')
]