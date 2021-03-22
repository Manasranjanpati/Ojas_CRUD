from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Student(models.Model):
    fullname = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    
