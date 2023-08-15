from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    
    path('students/', views.student_list, name='student-list'),
    path('register-student/', views.register_student, name='register-student'),
    path('update-student/<int:pk>/', views.update_student, name='update-student'),
    path('delete/<int:pk>/', views.delete_student, name='delete-student'),
]