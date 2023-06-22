from django.shortcuts import render
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

        contact = Contact(name=name, email=email, comment=comment)
        contact.save()

    return render(request, 'Home/contact.html')