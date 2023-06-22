from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('post/', views.createGraph, name='dataInput'),
    path('display/<int:snum>/', views.displayGraph, name='displayGraph')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

