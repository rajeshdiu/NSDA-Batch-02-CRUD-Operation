from django.db import models

class Student_Models(models.Model):
    
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.FirstName
    
    
class Teacher_Model(models.Model):
    
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.FirstName
    
    
class Employee_Model(models.Model):
    
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.FirstName

class Staff_Model(models.Model):
    
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=100)
    
    def __str__(self) :
        return self.FirstName+ " "+ self.LastName