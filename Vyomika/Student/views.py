from django.shortcuts import render, HttpResponse
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
        stdemail = request.POST.get('srdemail')
        stdadd = request.POST.get('stdadd')
        stdphone = request.POST.get('stdphone')
        stdfaculty = request.POST.get('stdfaculty')
        stdgender = request.POST.get('stdgender')

        student = Student(stdname=stdname, stdemail=stdemail, stdadd=stdadd,
                          stdphone=stdphone, stdfaculty=stdfaculty, stdgender=stdgender)
        
        student.save()
        stdData = {'stdname':stdname, 'stdemail':stdemail, 'stdadd':stdadd, 'stdphone':stdphone, 'stdfaculty':stdfaculty, 'stdgender':stdgender}

    return render(request, 'Student/addstd.html')