from django.db import models

# Create your models here. 
class Student(models.Model):
    studentId = models.CharField(max_length=12, primary_key = True)
    studentName = models.CharField(max_length = 128)
    studentPhone = models.CharField(max_length = 128)

 