from django.shortcuts import render
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')

# Create your views here.

def home(request):
    return render(request, 'Home/index.html')

def about(request):
    return render(request, 'Home/about.html')
    
def contactUs(request):
    return render(request, 'Home/contact.html')