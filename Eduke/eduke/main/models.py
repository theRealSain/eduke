from django.db import models


class Institution(models.Model):
    institution_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    institution_name = models.CharField(max_length=255)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.institution_name


class Classes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    institution_id = models.ForeignKey(Institution, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Subjects(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Users(models.Model):
    TEACHER = 'teacher'
    STUDENT = 'student'
    PARENT = 'parent'

    ROLE_CHOICES = [
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
        (PARENT, 'Parent'),
    ]

    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.role} - {self.id}"


class Teachers(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    class_id = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True, blank=True)
    institution_id = models.ForeignKey(Institution, on_delete=models.CASCADE)
    user_id = models.OneToOneField(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    
class Students(models.Model):
    id = models.AutoField(primary_key=True)
    roll_no = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    class_id = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True, blank=True)
    user_id = models.OneToOneField(Users, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.roll_no})"


class Parents(models.Model):
    id = models.AutoField(primary_key=True)
    # Use on_delete=models.CASCADE to ensure cascading deletes when the student is deleted
    student_roll_no = models.OneToOneField(Students, on_delete=models.CASCADE, to_field="roll_no")
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.OneToOneField(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.name if self.name else f"Parent of {self.student_roll_no}"



class Marks(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    mark_percentage = models.FloatField()

    def __str__(self):
        return f"{self.student_id} - {self.subject_id} - {self.mark_percentage}%"


class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.student_id} - {self.attendance_date} - {self.status}"


class StudentEvaluations(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    study_time_rating = models.IntegerField()
    sleep_time_rating = models.IntegerField()
    stress_handling_rating = models.IntegerField()
    homework_completion_rating = models.IntegerField()
    class_participation_rating = models.IntegerField()
    focus_rating = models.IntegerField()
    test_preparation_rating = models.IntegerField()
    class_difficulty_rating = models.IntegerField()
    parent_rating = models.IntegerField()
    teacher_rating = models.IntegerField()

    def __str__(self):
        return f"Evaluation for {self.student_id}"


class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField()
    sender_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="sent_messages")
    receiver_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="received_messages")

    def __str__(self):
        return f"Chat from {self.sender_id} to {self.receiver_id}"


class Quizzes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    class_id = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True, blank=True)
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    question = models.TextField()
    option_a = models.CharField(max_length=255, null=True)
    option_b = models.CharField(max_length=255, null=True)
    option_c = models.CharField(max_length=255, null=True)
    option_d = models.CharField(max_length=255, null=True)
    correct_option = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], null=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    student_response = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='A')

    def __str__(self):
        return f"Quiz {self.id} - {self.name}"
