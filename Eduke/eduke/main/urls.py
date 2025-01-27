from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('login/', views.login_view, name='login'),  # Login page
    path('register/', views.register_institution, name='institution_register'),  # Registration page
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),  # Admin dashboard
    path('admin/classes/', views.admin_classes, name='admin_classes'), # Admin classes
    path('admin/teachers/', views.admin_teachers, name='admin_teachers'), # Admin teachers
    path('admin/students/', views.admin_students, name='admin_students'), # Admin students
    path('admin/profile/', views.admin_profile, name='admin_profile'),
    path('admin/logout/', views.logout, name='logout'),  # Admin logout

    path('teacher/login/', views.teacher_login_view, name='teacher_login'), # Teacher login
    path('teacher/dashboard/', views.teacher_dashboard_view, name='teacher_dashboard'), # Teacher dashboard
    path('teacher/students/', views.teacher_students, name='teacher_students'),
    path('teacher/class/', views.teacher_class, name='teacher_class'),
    path('teacher/profile/', views.teacher_profile, name='teacher_profile'),

    path('student/login/', views.student_login, name='student_login'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student/class/', views.student_class, name='student_class'),
    path('student/profile/', views.student_profile, name='student_profile'),

    path('parent/login/', views.parent_login, name='parent_login'),
    path('parent/dashboard/', views.parent_dashboard, name='parent_dashboard'),
    path('parent_teacher_profile/', views.parent_teacher_profile, name='parent_teacher_profile'),
    path('parent/profile/', views.parent_profile, name='parent_profile'),
]
