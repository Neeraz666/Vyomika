from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

# Create your views here.
def signupPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        passsword2 = request.POST.get('password2')

        if password1 == passsword2:
            if UserAccount.objects.filter(email=email).exists:
                messages.error(request, 'Email already exists!')
                return redirect('/signup')
            
            else:
                if len(username) < 6 and not username.isalnum():
                    messages.error(request, 'Username must be at least 6 letters and should only contain alphanumeric.')
                    return redirect('/signup')
                
                else:
                    user = UserAccount.objects.create_user(email=email, username=username)
                    user.email = email
                    user.username  = username
                    user.password = make_password(password1)

                    user.save()

                    messages.success(request, "Thank you. Your account has been created successfully.")

                    return redirect('/login')

        else:
            messages.error(request, 'Passwords do not match!. please try again!')
            return redirect('/signup')
        
def loginPage(reqest):
    return HttpResponse("Login page")