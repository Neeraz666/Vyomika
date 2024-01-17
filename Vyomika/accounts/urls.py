from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='loginpage'),
    path('signup/', views.signupPage, name='signuppage'),
    path('handlesignup', views.signup, name='signup'),
]