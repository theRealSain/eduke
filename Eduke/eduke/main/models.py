from django.db import models

# Institution Model
class Institution(models.Model):
    id = models.AutoField(primary_key=True)  # This is the auto-incremented ID
    email = models.EmailField(unique=True)
    institution_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.institution_name

# Classes Model
class Classes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Subjects Model
class Subjects(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    class_obj = models.ForeignKey(Classes, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Teachers Model
class Teachers(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    class_obj = models.ForeignKey(Classes, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)

    def __str__(self):
        return self.email

# Students Model
class Students(models.Model):
    id = models.AutoField(primary_key=True)
    roll_no = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    class_obj = models.ForeignKey(Classes, on_delete=models.CASCADE)
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)

    def __str__(self):
        return self.roll_no

# Parents Model
class Parents(models.Model):
    id = models.AutoField(primary_key=True)
    student_roll_no = models.ForeignKey(Students, on_delete=models.CASCADE, to_field='roll_no')
    password = models.CharField(max_length=255)
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)

    def __str__(self):
        return f"Parent of {self.student_roll_no}"

# Marks Model
class Marks(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    mark_percentage = models.FloatField()

    def __str__(self):
        return f"{self.student} - {self.subject.name}"

# Attendance Model
class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')])

    def __str__(self):
        return f"{self.student} - {self.status} on {self.attendance_date}"

# Student Evaluations Model
class StudentEvaluations(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    study_time_rating = models.FloatField()
    sleep_time_rating = models.FloatField()
    stress_handling_rating = models.FloatField()
    homework_completion_rating = models.FloatField()
    class_participation_rating = models.FloatField()
    focus_rating = models.FloatField()
    test_preparation_rating = models.FloatField()
    class_difficulty_rating = models.FloatField()
    parent_rating = models.FloatField()
    teacher_rating = models.FloatField()

    def __str__(self):
        return f"Evaluation of {self.student}"

# Chat Model
class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField()
    sender = models.ForeignKey('Users', on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey('Users', on_delete=models.CASCADE, related_name="received_messages")

    def __str__(self):
        return f"Message from {self.sender.email} to {self.receiver.email}"

# Users Model
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=[('teacher', 'Teacher'), ('student', 'Student'), ('parent', 'Parent')])

    def __str__(self):
        return self.email

# Quizzes Model
class Quizzes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    class_obj = models.ForeignKey(Classes, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Questions and Responses Model
class QuestionsResponses(models.Model):
    id = models.AutoField(primary_key=True)
    quiz = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    question = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    student_response = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])

    def __str__(self):
        return f"Response from {self.student.roll_no} for quiz {self.quiz.name}"
