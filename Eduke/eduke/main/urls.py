from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('login/', views.login_view, name='login'),  # Login page
    path('register/', views.register_institution, name='institution_register'),  # Registration page
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),  # Admin dashboard
    path('admin/classes/', views.admin_classes, name='admin_classes'), # Admin classes
    path('class/edit/<int:class_id>/', views.admin_class_edit, name='admin_class_edit'), # Admin class edit
    path('admin/class/<int:class_id>/', views.admin_class_detail, name='admin_class_detail') , # Admin class detail
    path('admin/subjects/', views.admin_subjects, name='admin_subjects'), # Admin subjects
    path('subject/edit/<int:subject_id>/', views.admin_subject_edit, name='admin_subject_edit'), # Admin subject edit
    path('admin/subject/<int:subject_id>/', views.admin_subject_detail, name='admin_subject_detail'), # Admin subject detail
    path('admin/students/', views.admin_students, name='admin_students'), # Admin students
    path('student/edit/<int:student_id>/', views.admin_student_edit, name='admin_student_edit'), # Admin student edit
    path('admin/student/<int:student_id>/', views.admin_student_performance, name='admin_student_performance'), # Admin student detail
    path('admin/profile/', views.admin_profile, name='admin_profile'),
    path('admin/logout/', views.logout, name='logout'),  # Admin logout
    
    path('upload_classes/', views.upload_classes, name='upload_classes'),
    path('upload_subjects/', views.upload_subjects, name='upload_subjects'),
    path('upload_students/', views.upload_students, name='upload_students'),

    path('class_head/login/', views.class_head_login, name='class_head_login'), # Class Head login
    path('class_head/dashboard/', views.class_head_dashboard, name='class_head_dashboard'), # Class Head dashboard
    path('class_head/class/', views.class_head_class, name='class_head_class'), # Class Head class
    path('class_head/students/', views.class_head_students, name='class_head_students'), # Class Head students
    path('class_head/profile/', views.class_head_profile, name='class_head_profile'), # Class Head profile
    path('class_head/class_head_chat/', views.class_head_chat, name='class_head_chat'), # Class Head chat
    path("class_head/class_head_chat_user/<int:user_id>/", views.class_head_chat_user, name="class_head_chat_user"), # Class Head chat user
    path('class_head/student_performance/<int:student_id>/', views.class_head_student_performance, name='class_head_student_performance'), # Class Head Student Performance
    path("update-attendance/", views.update_attendance, name="update_attendance"),
    path('delete-attendance/', views.delete_attendance, name="delete_attendance"),

    path('subject_head/login/', views.subject_head_login, name='subject_head_login'), # Subject Head login
    path('subject_head/dashboard/', views.subject_head_dashboard, name='subject_head_dashboard'), # Subject Head dashboard
    path('subject_head/profile/', views.subject_head_profile, name='subject_head_profile'), # Subject Head Profile
    path('subject_head/class/', views.subject_head_class, name='subject_head_class'), # Subject Head Class
    path('subject_head/subjects/', views.subject_head_subjects, name='subject_head_subjects'), # Subject Head Subjects
    path('subject_head/chat/', views.subject_head_chat, name='subject_head_chat'), # Subject Head Chat
    path('subject_head/chat/<int:user_id>/', views.subject_head_chat_user, name='subject_head_chat_user'),
    path('subject_head/quiz/', views.subject_head_quiz, name='subject_head_quiz'), # Subject Head Quiz
    path('subject_head/study_materials/', views.subject_head_studys, name='subject_head_studys'), # Subject Head Study Materials
    path('subject_head/marks/', views.subject_head_marks, name='subject_head_marks'), # Subject Head Marks
    path('download-marks-template/<int:subject_id>/', views.download_marks_template, name='download_marks_template'),
    path('upload-marks/', views.upload_marks, name='upload_marks'),
    path('subject_head/attendance/', views.subject_head_attendance, name='subject_head_attendance'), # Subject Head Attendance
    path('subject_head/attendance_history/', views.subject_head_attendance_history, name='subject_head_attendance_history'), # Subject Head Attendance History
    path('subject_head/evaluation/', views.subject_head_evaluation, name='subject_head_evaluation'), # Subject Head Evaluation
    path('subject_head/students/<int:student_id>/', views.subject_head_students, name='subject_head_students'), # Subject Head Performance

    path('student/login/', views.student_login, name='student_login'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student/class/', views.student_class, name='student_class'),
    path('student/profile/', views.student_profile, name='student_profile'),
    path('student/student_chat/', views.student_chat, name='student_chat'),
    path('student/chat/<int:user_id>/', views.student_chat_user, name='student_chat_user'),
    path('student/subject/<int:subject_id>/', views.student_subject_detail, name='student_subject_detail'), # Subject Detail
    path('student/quiz/<int:subject_id>/<int:quiz_id>/', views.student_quiz, name='student_quiz'), # Quiz
    path('student/performance/', views.student_performance, name='student_performance'),
    path('student/eduke_bot/', views.student_eduke_bot, name='student_eduke_bot'),
    path('student/prediction/', views.student_prediction, name='student_prediction'),

    path('parent/login/', views.parent_login, name='parent_login'),
    path('parent/dashboard/', views.parent_dashboard, name='parent_dashboard'),
    path('parent_teacher_profile/', views.parent_teacher_profile, name='parent_teacher_profile'),
    path('parent/class/', views.parent_class, name='parent_class'),
    path('parent/profile/', views.parent_profile, name='parent_profile'),
    path('parent/parent_chat/', views.parent_chat, name='parent_chat'),
    path('parent_chat/<int:user_id>/', views.parent_chat_user, name='parent_chat_user'),
    path('parent/evaluation/', views.parent_evaluation, name='parent_evaluation'),
    path('parent/student_performance/', views.parent_student_performance, name='parent_student_performance'),
    path('parent/eduke_bot/', views.parent_eduke_bot, name='parent_eduke_bot'),
    path('parent/prediction/', views.parent_prediction, name='parent_prediction'),

    path('api/predict_marks/', views.predict_marks, name='predict_marks'),

]   
