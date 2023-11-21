
from django.contrib import admin
from django.urls import path
from myProject import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage/',views.homePage,name="homePage"),
    path('studentPage/',views.studentPage,name="studentPage"),
    path('teacherPage/',views.teacherPage,name="teacherPage"),
    path('employeePage/',views.employeePage,name="employeePage"),
    
    path('addStudent/',views.addStudent,name="addStudent"),
    
]
