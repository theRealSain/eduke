from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('login/', views.login_view, name='login'),  # Login page
    path('register/', views.register_institution, name='institution_register'),  # Registration page
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),  # Admin dashboard
    path('admin/classes/', views.admin_classes, name='admin_classes'), # Admin classes
    path('admin/subjects/', views.admin_subjects, name='admin_subjects'), # Admin subjects
    path('admin/students/', views.admin_students, name='admin_students'), # Admin students
    path('admin/profile/', views.admin_profile, name='admin_profile'),
    path('admin/logout/', views.logout, name='logout'),  # Admin logout

    path('class_head/login/', views.class_head_login, name='class_head_login'), # Class Head login
    path('class_head/dashboard/', views.class_head_dashboard, name='class_head_dashboard'), # Class Head dashboard
    path('class_head/class/', views.class_head_class, name='class_head_class'), # Class Head class
    path('class_head/students/', views.class_head_students, name='class_head_students'), # Class Head students
    path('class_head/subjects/', views.class_head_subjects, name='class_head_subjects'), # Class Head subjects
    path('class_head/profile/', views.class_head_profile, name='class_head_profile'), # Class Head profile
    path('class_head/class_head_chat/', views.class_head_chat, name='class_head_chat'), # Class Head chat
    path("class_head/class_head_chat_user/<int:user_id>/", views.class_head_chat_user, name="class_head_chat_user"), # Class Head chat user
    path('class_head/student_profile/<int:roll_no>/', views.class_head_student_profile, name='class_head_student_profile'), # Class Head Student Profile

    path('subject_head/login/', views.subject_head_login, name='subject_head_login'), # Subject Head login
    path('subject_head/dashboard/', views.subject_head_dashboard, name='subject_head_dashboard'), # Subject Head dashboard
    path('subject_head/profile/', views.subject_head_profile, name='subject_head_profile'), # Subject Head Profile
    path('subject_head/class/', views.subject_head_class, name='subject_head_class'), # Subject Head Class
    path('subject_head/subjects/', views.subject_head_subjects, name='subject_head_subjects'), # Subject Head Subjects
    path('subject_head/chat/', views.subject_head_chat, name='subject_head_chat'), # Subject Head Chat
    path('subject_head/chat/<int:user_id>/', views.subject_head_chat_user, name='subject_head_chat_user'),
    path('subject_head/quiz/', views.subject_head_quiz, name='subject_head_quiz'), # Subject Head Quiz
    path('subject_head/study_materials/', views.subject_head_studys, name='subject_head_studys'), # Subject Head Study Materials

    path('student/login/', views.student_login, name='student_login'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student/class/', views.student_class, name='student_class'),
    path('student/profile/', views.student_profile, name='student_profile'),
    path('student/student_chat/', views.student_chat, name='student_chat'),
    path('student/chat/<int:user_id>/', views.student_chat_user, name='student_chat_user'),
    path('student/subject/<int:subject_id>/', views.student_subject_detail, name='student_subject_detail'), # Subject Detail
    path('student/quiz/<int:subject_id>/<int:quiz_id>/', views.student_quiz, name='student_quiz'), # Quiz

    path('parent/login/', views.parent_login, name='parent_login'),
    path('parent/dashboard/', views.parent_dashboard, name='parent_dashboard'),
    path('parent_teacher_profile/', views.parent_teacher_profile, name='parent_teacher_profile'),
    path('parent_class/', views.parent_class, name='parent_class'),
    path('parent/profile/', views.parent_profile, name='parent_profile'),
    path('parent/parent_chat/', views.parent_chat, name='parent_chat'),
    path('parent_chat/<int:user_id>/', views.parent_chat_user, name='parent_chat_user')

]   
