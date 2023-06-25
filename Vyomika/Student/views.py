from django.shortcuts import render, HttpResponse

# Create your views here.
def management(request):
    return render(request, 'Student/home.html')

def faculty(request):
    return render(request, 'Student/class.html')

def studentMgmt(request):
    return render(request, 'Student/stdmgmt.html')