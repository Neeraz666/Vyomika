from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.core.files.storage import default_storage
from .models import Student, Staff
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def management(request):
    return render(request, 'Student/home.html')

@login_required
def faculty(request):
    return render(request, 'Student/class.html')

@login_required
def addStudent(request, stdfaculty):
    if request.method == 'POST':
        stdname = request.POST.get('stdname')
        stdemail = request.POST.get('stdemail')
        stdadd = request.POST.get('stdadd')
        stdphone = request.POST.get('stdphone')
        stdfaculty = request.POST.get('stdfaculty')
        stdgender = request.POST.get('stdgender')
        stdimage = request.FILES.get('stdimage')
        
        currentuser = request.user

        student = Student(stdname=stdname, user=currentuser ,stdemail=stdemail, stdadd=stdadd,
                          stdphone=stdphone, stdfaculty=stdfaculty, stdgender=stdgender, stdimage =stdimage)
        
        student.save()
        # stdData = {'stdname':stdname, 'stdemail':stdemail, 'stdadd':stdadd, 'stdphone':stdphone, 'stdfaculty':stdfaculty, 'stdgender':stdgender}
        if stdfaculty == 'BSIT':
            return redirect('/management/faculty/bsitstudents/')
        elif stdfaculty == 'BBA':
            return redirect('/management/faculty/bbastudents/')

    return render(request, 'Student/addstd.html')

@login_required
def bsit(request):
    currentuser = request.user
    student = Student.objects.filter(stdfaculty='BSIT', user=currentuser)
    return render(request, 'Student/bsitstudents.html', {'student':student})

@login_required
def bba(request):
    currentuser = request.user
    student = Student.objects.filter(stdfaculty='BBA', user = currentuser)
    return render(request, 'Student/bbastudents.html', {'student':student})

@login_required
def staff(request):
    currentuser = request.user
    staff = Staff.objects.filter(user=currentuser)
    return render(request, 'Student/staffmgmt.html', {'staff':staff})

@login_required
def addStaff(request):
    if request.method == 'POST':
        stfname = request.POST.get('stfname')
        stfemail = request.POST.get('stfemail')
        stfadd = request.POST.get('stfadd')
        stfphone = request.POST.get('stfphone')
        stfrole = request.POST.get('stfrole')
        stfgender = request.POST.get('stfgender')
        stfimage = request.FILES.get('stfimage')

        currentuser = request.user

        staff = Staff(stfname=stfname, user=currentuser,stfemail=stfemail, stfadd=stfadd,
                          stfphone=stfphone, stfrole=stfrole, stfgender=stfgender, stfimage =stfimage)
        staff.save()

        return redirect('/management/staff/')


    return render(request, 'Student/addstaff.html')

@login_required
def delete_staff(request, stf_id):
    staff = get_object_or_404(Staff, stf_id=stf_id)
    staff.delete()

    return redirect('/management/staff/')

@login_required
def delete_student(request, std_id):
    student = get_object_or_404(Student, std_id=std_id)
    student.delete()

    if student.stdfaculty == 'BSIT':
        return redirect('/management/faculty/bsitstudents/')
    elif student.stdfaculty == 'BBA':
        return redirect('/management/faculty/bbastudents/')
    
@login_required
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

@login_required
def searchStf(request):
    query = request.GET.get('query', '')    


    if len(query)>78:
        allStf = Staff.objects.none()
    else:
        stfName = Staff.objects.filter(stfname__icontains=query)
        stfEmail = Staff.objects.filter(stfemail__icontains=query)
        stfAdd = Staff.objects.filter(stfadd__icontains=query)
        allStf = stfName.union(stfEmail, stfAdd)

    if allStf.count() == 0:
        messages.warning(request, "No search results d. Please check your query.")
         
    params = {"allStf": allStf, 'query':query}
    return render(request, 'Student/searchStf.html', params)