from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import make_password

# Create your views here.
def signupPage(request):
    return render(request, 'accounts/signup.html')

def loginPage(request):
    return render(request, 'accounts/login.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if UserAccount.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists!')
                return redirect('/login/signup')
            
            else:
                if len(username) < 6 and not username.isalnum():
                    messages.error(request, 'Username must be at least 6 letters and should only contain alphanumeric.')
                    return redirect('/login/signup')
                
                else:
                    user = UserAccount.objects.create_user(email=email, username=username, password = password1)
                    user.save()

                    messages.success(request, "Thank you. Your account has been created successfully.")

                    return redirect('/login')

        else:
            messages.error(request, 'Passwords do not match!. please try again!')
            return redirect('/login/signup')
        
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)

        if user:
            auth_login(request, user)
            messages.success(request,f"Hello {user.get_username()}, Welcome to Vyomika")
            return redirect("/")
        else:
            messages.error(request,"Invalid Username or password.")
            return redirect("/login")

    else:
        return HttpResponse("This view only accepts POST requests.")
    

def handlelogout(request):
    logout(request)
    messages.success(request,"Logged out successfully.")

    return redirect("/")