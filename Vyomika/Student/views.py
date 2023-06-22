from django.shortcuts import render, HttpResponse

# Create your views here.
def management(request):
    return render(request, 'Student/home.html')