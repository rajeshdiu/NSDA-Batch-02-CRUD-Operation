
from django.contrib import admin
from django.urls import path
from myProject import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('indexPage/',views.indexPage,name="indexPage"),
    path('homePage/',views.homePage,name="homePage"),
    path('studentPage/',views.studentPage,name="studentPage"),
    path('teacherPage/',views.teacherPage,name="teacherPage"),
    path('employeePage/',views.employeePage,name="employeePage"),
    
    path('addStudent/',views.addStudent,name="addStudent"),
    path('editStudent/<str:id>',views.editStudent,name="editStudent"),
    path('updateStudent/',views.updateStudent,name="updateStudent"),
    
    
    path('ediiTeacher/<str:id>',views.ediiTeacher,name="ediiTeacher"),
    path('updateTeacher/',views.updateTeacher,name="updateTeacher"),
    
    
    
    
    path('addEmployee/',views.addEmployee,name="addEmployee"),
    path('editEmployee/<str:id>',views.editEmployee,name="editEmployee"),
    
    
    path('staffPage/',views.staffPage,name="staffPage"),
    path('addStaff/',views.addStaff,name="addStaff"),
    path('editStaff/<str:id>',views.editStaff,name="editStaff"),
    path('updateStaff/',views.updateStaff,name="updateStaff"),
    
]
