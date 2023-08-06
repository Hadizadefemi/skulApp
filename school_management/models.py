from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Class(models.Model):
    class_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.class_name


class Student(models.Model):
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=1, choices=GENDER_CHOICE)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    state_of_origin = models.CharField(max_length=20)
    address = models.TextField()
    guardian_contact = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    date_joined = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class_owner = models.OneToOneField(Class, on_delete=models.PROTECT)
    
    def __str__(self):
        return f'{self.user}'


class Attendance(models.Model):
    ATTENDANCE_CHOICE = (
        ('A', 'Absent'),
        ('P', 'Present'),
    )
    
    student = models.ForeignKey(Student, models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=1, choices=ATTENDANCE_CHOICE)
    
    def __str__(self):
        return f"{self.student} - {self.get_status_display()} - {self.date}"