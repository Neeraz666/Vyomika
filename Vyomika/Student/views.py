from django.shortcuts import render, HttpResponse, redirect
from django.core.files.storage import default_storage
from .models import Student

# Create your views here.


def management(request):
    return render(request, 'Student/home.html')


def faculty(request):
    return render(request, 'Student/class.html')


def studentMgmt(request):
    return render(request, 'Student/stdmgmt.html')

def addStudent(request):
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
        return redirect('/management/faculty/student/')

    return render(request, 'Student/addstd.html')