from django.shortcuts import render
from django.contrib import messages
from .models import Contact

# Create your views here.

def home(request):
    return render(request, 'Home/index.html')

def about(request):
    return render(request, 'Home/about.html')
    
def contactUs(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        
        if len(name)<2 or len(email)<3 or len(comment)<5:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, comment=comment)
            contact.save()
            messages.success(request, "Your message has been successfully sent")

    return render(request, 'Home/contact.html')

def handleSignup(request):
    pass