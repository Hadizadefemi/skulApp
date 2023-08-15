from django.contrib import admin
from .models import Student, Teacher, Class, Attendance

# Register your models here.
admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Attendance)
admin.site.register(Teacher)
#admin.site.register(Subject)