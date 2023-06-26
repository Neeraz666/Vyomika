from django.shortcuts import render, HttpResponse, redirect
from django.core.files.storage import default_storage
from .models import Student

# Create your views here.


def management(request):
    return render(request, 'Student/home.html')


def faculty(request):
    return render(request, 'Student/class.html')

def addStudent(request, stdfaculty):
    if request.method == 'POST':
        stdname = request.POST.get('stdname')
        stdemail = request.POST.get('stdemail')
        stdadd = request.POST.get('stdadd')
        stdphone = request.POST.get('stdphone')
        stdfaculty = request.POST.get('stdfaculty')
        stdgender = request.POST.get('stdgender')
        stdimage = request.FILES.get('stdimage')

        student = Student(stdname=stdname, stdemail=stdemail, stdadd=stdadd,
                          stdphone=stdphone, stdfaculty=stdfaculty, stdgender=stdgender, stdimage =stdimage)
        
        student.save()
        # stdData = {'stdname':stdname, 'stdemail':stdemail, 'stdadd':stdadd, 'stdphone':stdphone, 'stdfaculty':stdfaculty, 'stdgender':stdgender}
        if stdfaculty == 'BSIT':
            return redirect('/management/faculty/bsitstudents/')
        elif stdfaculty == 'BBA':
            return redirect('/management/faculty/bbastudents/')

    return render(request, 'Student/addstd.html')

def bsit(request):
    student = Student.objects.filter(stdfaculty='BSIT')
    return render(request, 'Student/bsitstudents.html', {'student':student})

def bba(request):
    student = Student.objects.filter(stdfaculty='BBA')
    return render(request, 'Student/bbastudents.html')
    # return render(request, 'Student/bbastudents.html')