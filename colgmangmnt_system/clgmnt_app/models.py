from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    corse_name=models.CharField(max_length=255)
    fee=models.IntegerField()

class Student(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    student_name=models.CharField(max_length=255)
    age=models.IntegerField()
    address=models.CharField(max_length=255)
    joining_date=models.DateField()
    email=models.EmailField()

class Usermember(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    age=models.IntegerField()
    address=models.CharField(max_length=255)
    image=models.ImageField(upload_to="image/",null=True)
    

    
