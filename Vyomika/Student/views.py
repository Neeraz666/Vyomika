from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.core.files.storage import default_storage
from .models import Student, Staff
from django.contrib import messages

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
    return render(request, 'Student/bbastudents.html', {'student':student})

def staff(request):
    staff = Staff.objects.all()
    return render(request, 'Student/staffmgmt.html', {'staff':staff})

def addStaff(request):
    if request.method == 'POST':
        stfname = request.POST.get('stfname')
        stfemail = request.POST.get('stfemail')
        stfadd = request.POST.get('stfadd')
        stfphone = request.POST.get('stfphone')
        stfrole = request.POST.get('stfrole')
        stfgender = request.POST.get('stfgender')
        stfimage = request.FILES.get('stfimage')

        staff = Staff(stfname=stfname, stfemail=stfemail, stfadd=stfadd,
                          stfphone=stfphone, stfrole=stfrole, stfgender=stfgender, stfimage =stfimage)
        staff.save()

        return redirect('/management/staff/')


    return render(request, 'Student/addstaff.html')

def delete_staff(request, stf_id):
    staff = get_object_or_404(Staff, stf_id=stf_id)
    staff.delete()

    return redirect('/management/staff/')

def delete_student(request, std_id):
    student = get_object_or_404(Student, std_id=std_id)
    student.delete()

    if student.stdfaculty == 'BSIT':
        return redirect('/management/faculty/bsitstudents/')
    elif student.stdfaculty == 'BBA':
        return redirect('/management/faculty/bbastudents/')
    

def searchStd(request, stdfaculty):
    stdfaculty = Student.objects.filter(stdfaculty=stdfaculty)
    query = request.GET.get('query', '')    


    if len(query)>78:
        allStd = Student.objects.none()
    else:
        allName = Student.objects.filter(stdname__icontains=query)
        allEmail = Student.objects.filter(stdemail__icontains=query)
        allAdd = Student.objects.filter(stdadd__icontains=query)
        allStd = allName.union(allEmail, allAdd)

    if allStd.count() == 0:
        messages.warning(request, "No search results found. Please check your query.")
         
    params = {"allStd": allStd, 'query':query}
    return render(request, 'Student/search.html', params)