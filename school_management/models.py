from django.db import models
from django.contrib.auth.models import User

# Create your models here.

    

class Class(models.Model):
    class_name = models.CharField(max_length=30)
    # subjects = models.ManyToManyField(Subject)
    
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
    
    class Meta:
        ordering = ['first_name', 'last_name']
    

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class_owner = models.OneToOneField(Class, on_delete=models.PROTECT)
    
    def __str__(self):
        return f'{self.user}'
    


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=None)
    date = models.DateField()
    is_present = models.BooleanField(default=False)
