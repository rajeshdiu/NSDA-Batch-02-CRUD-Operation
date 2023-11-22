from django.shortcuts import redirect,render

from myApp.models import *


def indexPage(request):
    
    return render(request,"index.html")
    


def homePage(request):
    
    return render(request,"home.html")


def studentPage(request):
    
    student=Student_Models.objects.all()
    
    context={
        'student':student,
    }
    
    return render(request,"student.html",context)

def teacherPage(request):
    
    teacher=Teacher_Model.objects.all()
    
    context={
        'student':teacher,
    }
    
    return render(request,"teacher.html",context)



def employeePage(request):
    
    employee=Employee_Model.objects.all()
    
    context={
        'employee':employee,
    }
    
    
    return render(request,"employee.html",context)


def addTeacher(request):
    
    if request.method=="POST":
        fname=request.POST.get("firstname")
        lname=request.POST.get("lastname")
        phone=request.POST.get("mobile")
        
        student=Teacher_Model(
            FirstName=fname,
            LastName=lname,
            Mobile=phone,
        )
        student.save()
        
        return redirect("teacherPage")
        
    return render(request,"teacher.html")


def ediiTeacher(request,id):
    
    teacher=Teacher_Model.objects.filter(id=id)
    
    context={
        'teacher':teacher,
    }
    

    return render(request,"ediiTeacher.html",context)

def updateTeacher(request):
    
    if request.method=="POST":
        teacher_id=request.POST.get("teacherid")
        fname=request.POST.get("firstname")
        lname=request.POST.get("lastname")
        phone=request.POST.get("mobile")
        
        teacher=Teacher_Model(
            id=teacher_id,
            FirstName=fname,
            LastName=lname,
            Mobile=phone,
        )
        teacher.save()
        
        return redirect("teacherPage")


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

def editStudent(request,id):
    
    student=Student_Models.objects.filter(id=id)
    context = {
        "student":student,
    }
    
    return render(request,"editStudent.html",context)

def updateStudent(request):

    if request.method=="POST":
        student_id=request.POST.get("studentid")
        fname=request.POST.get("firstname")
        lname=request.POST.get("lastname")
        phone=request.POST.get("mobile")
        
        student=Student_Models(
            id=student_id,
            FirstName=fname,
            LastName=lname,
            Mobile=phone,
        )
        student.save()
        
        return redirect("studentPage")
        
    return render(request,"student.html")


def addEmployee(request):
    
    if request.method=="POST":
        fname=request.POST.get("firstname")
        lname=request.POST.get("lastname")
        phone=request.POST.get("mobile")
        
        employee=Employee_Model(
            FirstName=fname,
            LastName=lname,
            Mobile=phone,
        )
        employee.save()
        
        return redirect("employeePage")
        
    return render(request,"employee.html")

def editEmployee(request,id):
    
    employee=Employee_Model.objects.filter(id=id)
    context = {
        "employee":employee,
    }
    
    return render(request,"editEmployee.html",context)


def updateStudent(request):

    if request.method=="POST":
        employee_id=request.POST.get("employeeid")
        fname=request.POST.get("firstname")
        lname=request.POST.get("lastname")
        phone=request.POST.get("mobile")
        
        employee=Employee_Model(
            id=employee_id,
            FirstName=fname,
            LastName=lname,
            Mobile=phone,
        )
        employee.save()
        
        return redirect("employeePage")
        
    return render(request,"employee.html")


def staffPage(request):
    
    staff=Staff_Model.objects.all()
    
    context={
        'staff':staff
    }
    
    
    return render(request,"staff.html",context)

def addStaff(request):
    
    
    
     if request.method=="POST":
        fname=request.POST.get("firstname")
        lname=request.POST.get("lastname")
        phone=request.POST.get("mobile")
        
        staff=Staff_Model(
            FirstName=fname,
            LastName=lname,
            Mobile=phone,
        )
        staff.save()
        
        return redirect("staffPage")

def editStaff(reqiest,id):
    
    staff=Staff_Model.objects.filter(id=id)
    
    context={
        'staff':staff,
    }
    
    
    return render(reqiest,"editStaff.html",context)


def updateStaff(request):
    
    
     if request.method=="POST":
        staff_id=request.POST.get("staffid")
        fname=request.POST.get("firstname")
        lname=request.POST.get("lastname")
        phone=request.POST.get("mobile")
        
        staff=Staff_Model(
            id=staff_id,
            FirstName=fname,
            LastName=lname,
            Mobile=phone,
        )
        staff.save()
        
        return redirect("staffPage")
    
    
    
    
    
