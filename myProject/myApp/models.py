from django.db import models

class Student_Models(models.Model):
    
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to="media/profile_pic",null=True)
    
    
    def __str__(self):
        return self.FirstName
    
    
class Teacher_Model(models.Model):
    
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to="media/profile_pic",null=True)
    
    
    def __str__(self):
        return self.FirstName
    
    
class Employee_Model(models.Model):
    
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to="media/profile_pic",null=True)
    
    
    def __str__(self):
        return self.FirstName

class Staff_Model(models.Model):
    
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to="media/profile_pic",null=True)
    
    def __str__(self) :
        return self.FirstName+ " "+ self.LastName

class Library_Model(models.Model):
    
    BookName=models.CharField(max_length=100)
    AuthorName=models.CharField(max_length=100)
    CountryName=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to="media/profile_pic",null=True)
    
    def __str__(self) :
        return self.BookName