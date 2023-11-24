from django.conf import settings
from django.conf.urls.static import static
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
    path('deleteStudent/<str:id>',views.deleteStudent,name="deleteStudent"),
    
    
    path('addTeacher/',views.addTeacher,name="addTeacher"),
    path('ediiTeacher/<str:id>',views.ediiTeacher,name="ediiTeacher"),
    path('updateTeacher/',views.updateTeacher,name="updateTeacher"),
    path('deleteTeacher/<str:id>',views.deleteTeacher,name="deleteTeacher"),
    
    path('addEmployee/',views.addEmployee,name="addEmployee"),
    path('editEmployee/<str:id>',views.editEmployee,name="editEmployee"),
    path('updateEmployee',views.updateEmployee,name="updateEmployee"),
    
    
    path('staffPage/',views.staffPage,name="staffPage"),
    path('addStaff/',views.addStaff,name="addStaff"),
    path('editStaff/<str:id>',views.editStaff,name="editStaff"),
    path('updateStaff/',views.updateStaff,name="updateStaff"),
    
    
    path('libraryPage/',views.libraryPage,name="libraryPage"),
    path('addLibrary/',views.addLibrary,name="addLibrary"),
    path('editLibrary/<str:id>',views.editLibrary,name="editLibrary"),
    path('updateLibrary',views.updateLibrary,name="updateLibrary"),
    path('deleteLibrary/<str:id>',views.deleteLibrary,name="deleteLibrary"),
    
    
    path('',views.loginPage,name="loginPage"),
    path('logoutPage',views.logoutPage,name="logoutPage"),
    path('signupPage/',views.signupPage,name="signupPage"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
