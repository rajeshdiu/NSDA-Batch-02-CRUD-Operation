from django.shortcuts import redirect,render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from myApp.models import *

def logoutPage(request):
    
    logout(request)
    
    return render(request,"login.html")

def loginPage(request):
    
    if request.method=='POST':
        
        username=request.POST.get("username")
        pass1=request.POST.get("password")
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request,user)
            return redirect("indexPage")
            
    return render(request,'login.html')

def signupPage(request):
    
    if request.method=='POST':
        
        username=request.POST.get("username")
        email=request.POST.get("email")
        pass1=request.POST.get("password1")
        pass2=request.POST.get("password2")
        
        if pass1!=pass2:
            return HttpResponse("Not Match")
        
        else:
            user = User.objects.create_user(username, email, pass1)
            user.save()
            return redirect("loginPage")
        
    return render(request,'signup.html')

@login_required
def indexPage(request):
    
    return render(request,"index.html")
    
@login_required
def homePage(request):
    
    return render(request,"home.html")

@login_required
def studentPage(request):
    
    student=Student_Models.objects.all()
    
    context={
        'student':student,
    }
    
    return render(request,"student.html",context)

@login_required
def teacherPage(request):
    
    teacher=Teacher_Model.objects.all()
    
    context={
        'student':teacher,
    }
    
    return render(request,"teacher.html",context)

@login_required
def employeePage(request):
    
    employee=Employee_Model.objects.all()
    
    context={
        'employee':employee,
    }
    
    return render(request,"employee.html",context)

@login_required
def addTeacher(request):
    
    my_message = {
        'add_failed': 'Teacher Add Failed',
        'add_Success': 'Teacher Add Successfully',
    }
    
    if request.method=="POST":
        fname=request.POST.get("firstname")
        lname=request.POST.get("lastname")
        phone=request.POST.get("mobile")
        profile_pic = request.FILES.get('profilepic')
        
        teacher=Teacher_Model(
            FirstName=fname,
            LastName=lname,
            Mobile=phone,
            profile_pic=profile_pic,
        )
        teacher.save()
        messages.success(request,my_message["add_Success"])
        
        return redirect("teacherPage")
        
    return render(request,"teacher.html")

@login_required
def ediiTeacher(request,id):
    
    teacher=Teacher_Model.objects.filter(id=id)
    
    context={
        'teacher':teacher,
    }
    return render(request,"ediiTeacher.html",context)

@login_required
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
    
@login_required 
def deleteTeacher(request,id):
    
    teacher=Teacher_Model.objects.filter(id=id)
    teacher.delete()
    
    return redirect("teacherPage")

@login_required
def addStudent(request):
    
    if request.method=="POST":
        fname=request.POST.get("firstname")
        lname=request.POST.get("lastname")
        phone=request.POST.get("mobile")
        profile_pic = request.FILES.get('profilepic')
     
        student=Student_Models(
            FirstName=fname,
            LastName=lname,
            Mobile=phone,
            profile_pic=profile_pic
        )
        student.save()
        
        return redirect("studentPage")
        
    return render(request,"student.html")

@login_required
def editStudent(request,id):
    
    student=Student_Models.objects.filter(id=id)
    context = {
        "student":student,
    }
    
    return render(request,"editStudent.html",context)

@login_required
def updateStudent(request):

    if request.method=="POST":
        student_id=request.POST.get("studentid")
        fname=request.POST.get("firstname")
        lname=request.POST.get("lastname")
        phone=request.POST.get("mobile")
        profilepic = request.FILES.get('profile_pic')
        
        student=Student_Models(
            id=student_id,
            FirstName=fname,
            LastName=lname,
            Mobile=phone,
            profile_pic=profilepic,
        )
        student.save()
        
        return redirect("studentPage")
        
    return render(request,"student.html")

@login_required
def deleteStudent(request,id):
    
    student=Student_Models.objects.filter(id=id)
    student.delete()
    
    return redirect("studentPage")

@login_required
def addEmployee(request):
    
    if request.method=="POST":
        fname=request.POST.get("firstname")
        lname=request.POST.get("lastname")
        phone=request.POST.get("mobile")
        profile_pic = request.FILES.get('profilepic')
        
        employee=Employee_Model(
            FirstName=fname,
            LastName=lname,
            Mobile=phone,
            profile_pic=profile_pic
        )
        employee.save()
        
        return redirect("employeePage")
        
    return render(request,"employee.html")

@login_required
def editEmployee(request,id):
    
    employee=Employee_Model.objects.filter(id=id)
    context = {
        "employee":employee,
    }
    
    return render(request,"editEmployee.html",context)

@login_required
def updateEmployee(request):

    if request.method=="POST":
        employee_id=request.POST.get("employeeid")
        fname=request.POST.get("firstname")
        lname=request.POST.get("lastname")
        phone=request.POST.get("mobile")
        profile_pic = request.FILES.get('profilepic')
        
        employee=Employee_Model(
            id=employee_id,
            FirstName=fname,
            LastName=lname,
            Mobile=phone,
            profile_pic=profile_pic,
        )
        employee.save()
        
        return redirect("employeePage")
        
    return render(request,"employee.html")

@login_required
def staffPage(request):
    
    staff=Staff_Model.objects.all()
    
    context={
        'staff':staff
    }
    
    
    return render(request,"staff.html",context)

@login_required
def addStaff(request):
    
     if request.method=="POST":
        fname=request.POST.get("firstname")
        lname=request.POST.get("lastname")
        phone=request.POST.get("mobile")
        profile_pic = request.FILES.get('profilepic')
        
        staff=Staff_Model(
            FirstName=fname,
            LastName=lname,
            Mobile=phone,
            profile_pic=profile_pic
        )
        staff.save()
        
        return redirect("staffPage")

@login_required
def editStaff(reqiest,id):
    
    staff=Staff_Model.objects.filter(id=id)
    
    context={
        'staff':staff,
    }
    
    
    return render(reqiest,"editStaff.html",context)

@login_required
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
    
@login_required  
def libraryPage(request):
    
    library=Library_Model.objects.all()
    
    context={
        'library':library,
    }
    return render(request,"library.html",context)

@login_required
def addLibrary(request):
    
     if request.method=="POST":
        book_name=request.POST.get("bookname")
        author_name=request.POST.get("authorname")
        country_name=request.POST.get("countryname")
        profile_pic = request.FILES.get('profilepic')
        
        library=Library_Model(
            BookName=book_name,
            AuthorName=author_name,
            CountryName=country_name,
            profile_pic=profile_pic
        )
        library.save()
        
        return redirect("libraryPage")
 
 
@login_required   
def editLibrary(request,id):
    
    library=Library_Model.objects.filter(id=id)
    
    context={
        'library':library,
    }
    
    return render(request,'editLibrary.html',context)

    
@login_required
def updateLibrary(request):
    
    
     if request.method=="POST":
        library_id=request.POST.get("libraryid")
        book_name=request.POST.get("bookname")
        author_name=request.POST.get("authorname")
        country_name=request.POST.get("countryname")
        
        library=Library_Model(
            id=library_id,
            BookName=book_name,
            AuthorName=author_name,
            CountryName=country_name,
        )
        library.save()
        
        return redirect("libraryPage")

@login_required 
def deleteLibrary(request,id):
    
    library=Library_Model.objects.filter(id=id)
    
    library.delete()
    
    return redirect("libraryPage")
