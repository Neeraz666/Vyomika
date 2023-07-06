from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import delete_student, delete_staff

urlpatterns = [
    path('', views.management, name='management'),
    path('faculty/', views.faculty, name='faculty'),
    path('staff/', views.staff, name='staff'),
    path('staff/addStaff/', views.addStaff, name='addStaff'),
    path('faculty/bsitstudents/', views.bsit, name = 'bsitstudent'),
    path('faculty/bbastudents/', views.bba, name = 'bbastudent'),
    path('faculty/<str:stdfaculty>/addStudent/', views.addStudent, name = 'addStudent'),
    path('faculty/<str:stdfaculty>/search/', views.searchStd, name = 'searchStd'),
    path('staff/searchstf/', views.searchStf, name = 'searchStd'),
    path('delete-student/<int:std_id>/', delete_student, name='delete_student'),
    path('delete-staff/<int:stf_id>/', delete_staff , name='delete_staff'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)