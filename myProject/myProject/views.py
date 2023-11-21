from django.shortcuts import redirect,render

from myApp.models import *


def homePage(request):
    
    return render(request,"home.html")


def studentPage(request):
    
    student=Student_Models.objects.all()
    
    context={
        'student':student,
    }
    
    return render(request,"student.html",context)

def teacherPage(request):
    
    return render(request,"teacher.html")



def employeePage(request):
    
    return render(request,"employee.html")


def addStudent(request):
    
    if request.method=="POST":
        fname=request.POST.get("firstname")
        lname=request.POST.get("lastname")
        phone=request.POST.get("mobile")
        
        student=Student_Models(
            FirstName=fname,
            LastName=lname,
            Mobile=phone,
        )
        student.save()
        
        return redirect("studentPage")
        
    return render(request,"student.html")

def updateStudent(request):
    
    student=Student_Models.objects.all()
    
    context={
        'student':student,
    }
    
    return render(request,"student.html",context)