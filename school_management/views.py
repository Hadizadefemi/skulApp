from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Student, Teacher
from .forms import StudentForm

# Create your views here.
def login_view(request):
    context = {}
    return render(request, 'school_management/login.html', context)

def student_list(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    students = Student.objects.filter(
        Q(first_name__icontains=q) |
        Q(last_name__icontains=q) |
        Q(state_of_origin__iexact=q) |
        Q(sex__exact=q)
        )
    num_student = Student.objects.all().count()
    males = Student.objects.filter(sex__exact='M').count()
    females = Student.objects.filter(sex__exact='F').count()
    
    context = {
        'students': students,
        'num_students': num_student,
        'males': males,
        'females': females,
        }
    return render(request, 'school_management/student_list.html', context)

def register_student(request):
    form = StudentForm()
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('student-list')
    
    context = {'form': form}
    return render(request, 'school_management/student_form.html', context)

def update_student(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
        return redirect('student-list')
    context = {"form": form}
    return render(request, 'school_management/student_form.html', context)

def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        return redirect('student-list')
    context = {'obj': student}
    return render(request, 'school_management/student_confirm_delete.html', context)

def teacher_list(request):
    teachers = Te
    context = {}
    return render(request, 'school_management/teacher_list.html', context)