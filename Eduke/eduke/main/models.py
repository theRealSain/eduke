from django.db import models

class Institution(models.Model):
    institution_id = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True)
    institution_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Users(models.Model):
    ROLE_CHOICES = [
        ('class_head', 'Class Head'),
        ('subject_head', 'Subject Head'),
        ('student', 'Student'),
        ('parent', 'Parent'),
    ]
    id = models.BigAutoField(primary_key=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

class Classes(models.Model):
    id = models.BigAutoField(primary_key=True)
    class_name = models.CharField(max_length=255)
    class_head = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

class Subjects(models.Model):
    id = models.BigAutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)
    subject_head = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    class_obj = models.ForeignKey(Classes, on_delete=models.CASCADE)

class Students(models.Model):
    id = models.BigAutoField(primary_key=True)
    roll_no = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True, null=True, blank=True)
    password = models.CharField(max_length=255)
    class_obj = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

class Parents(models.Model):
    id = models.BigAutoField(primary_key=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)  # Nullable, no unique constraint


class Attendance(models.Model):
    class StatusChoices(models.TextChoices):
        PRESENT = 'present', 'Present'
        ABSENT = 'absent', 'Absent'

    id = models.BigAutoField(primary_key=True)
    attendance_date = models.DateField()
    hour = models.PositiveSmallIntegerField()
    status = models.CharField(
        max_length=10, 
        choices=StatusChoices.choices,
        default=StatusChoices.PRESENT
    )
    student = models.ForeignKey('Students', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subjects', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class StudentEvaluation(models.Model):
    id = models.BigAutoField(primary_key=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    study_time_rating = models.FloatField(null=True)
    sleep_time_rating = models.FloatField(null=True)
    class_participation_rating = models.FloatField(null=True)
    academic_activity_rating = models.FloatField(null=True)
    attendance_percentage = models.FloatField(null=True)
    marks_percentage = models.FloatField(null=True)

class Chat(models.Model):
    id = models.BigAutoField(primary_key=True)
    message = models.TextField()
    sender = models.ForeignKey(Users, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Users, related_name='received_messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Quizzes(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    class_obj = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True, blank=True)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)

class QuizQuestions(models.Model):
    id = models.BigAutoField(primary_key=True)
    quiz = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    question = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])

class QuizResponse(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.ForeignKey(QuizQuestions, on_delete=models.CASCADE)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    student_response = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], null=True, blank=True)

class Announcements(models.Model):
    id = models.BigAutoField(primary_key=True)
    message = models.TextField()
    class_obj = models.ForeignKey(Classes, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class StudyMaterials(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_url = models.TextField(null=True, blank=True)
    announcement = models.TextField(null=True, blank=True)
    class_obj = models.ForeignKey(Classes, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
