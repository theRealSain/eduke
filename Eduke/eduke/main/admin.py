from django.contrib import admin
from .models import User, Class, Student, Teacher, Parent, Subject, Attendance, Marks, StudentEvaluation, Chat

# Register models here to manage them in Django's admin panel
admin.site.register(User)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Parent)
admin.site.register(Subject)
admin.site.register(Attendance)
admin.site.register(Marks)
admin.site.register(StudentEvaluation)
admin.site.register(Chat)
