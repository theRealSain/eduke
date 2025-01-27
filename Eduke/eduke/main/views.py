from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import InstitutionRegisterForm, LoginForm, AddClassForm, TeacherLoginForm, StudentLoginForm, ParentLoginForm
from .models import Institution, Classes, Teachers, Students, Users, Parents
from django.db import IntegrityError, transaction
from django.db import connection
from django.core.exceptions import ObjectDoesNotExist


# Index page
def index(request):
    return render(request, 'index.html')

# Admin Dashboard view
def admin_dashboard(request):
    # Check if the user is logged in
    if 'institution_id' not in request.session:
        messages.error(request, 'Please login to access the dashboard')
        return redirect('login')

    # Get the institution_id from the session
    institution_id = request.session['institution_id']
    
    try:
        # Fetch the institution based on the institution_id from the session
        institution = Institution.objects.get(institution_id=institution_id)

        # Current institution details
        institution_name = institution.institution_name
        password = institution.password
        email = institution.email
    except Institution.DoesNotExist:
        messages.error(request, "Institution not found.")
        return redirect('login')
    
    # Calculate the counts for the specific institution
    total_users = (
        Users.objects.filter(
            id__in=Teachers.objects.filter(institution_id=institution_id).values('user_id_id')
        ).count()
        + Users.objects.filter(
            id__in=Students.objects.filter(class_id__in=Classes.objects.filter(institution_id=institution_id).values('id')).values('user_id_id')
        ).count()
    )

    teacher_count = Teachers.objects.filter(institution_id=institution_id).count()

    # Get all classes belonging to the logged-in institution
    class_ids = Classes.objects.filter(institution_id=institution_id).values('id')

    # Count the students belonging to those classes
    student_count = Students.objects.filter(class_id__in=class_ids).count()

    total_classes = Classes.objects.filter(institution_id=institution_id).count()

    # Pass the counts to the template
    context = {
        'institution_name': institution_name,
        'total_users': total_users,
        'teacher_count': teacher_count,
        'student_count': student_count,
        'total_classes': total_classes,
    }

    return render(request, 'admin/admin_dashboard.html', context)

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Institution, Classes
from .forms import AddClassForm

def admin_classes(request):
    # Check if the user is logged in
    if 'institution_id' not in request.session:
        messages.error(request, 'Please log in to access this page.')
        return redirect('login')

    # Get the institution_id from the session
    institution_id = request.session['institution_id']

    try:
        # Fetch the institution based on the institution_id from the session
        institution = Institution.objects.get(institution_id=institution_id)
    except Institution.DoesNotExist:
        messages.error(request, "Institution not found.")
        return redirect('login')

    # Fetch all classes associated with the institution
    classes = Classes.objects.filter(institution_id=institution.institution_id)

    # Handle POST request to add a new class
    if request.method == 'POST':
        form = AddClassForm(request.POST)
        if form.is_valid():
            # Save the new class and associate it with the institution
            new_class = form.save(commit=False)
            new_class.institution_id = institution  # Set the foreign key to the institution
            new_class.save()
            messages.success(request, 'New class added successfully!')
            return redirect('admin_classes')  # Redirect to the same page to update the list
        else:
            messages.error(request, 'Error adding class. Please try again.')
    else:
        form = AddClassForm()

    # Prepare context for the template
    context = {
        'institution_name': institution.institution_name,
        'classes': classes,
        'form': form,
    }

    # Render the template
    return render(request, 'admin/admin_classes.html', context)


def admin_teachers(request):
    # Check if the user is logged in
    if 'institution_id' not in request.session:
        messages.error(request, 'Please log in to access this page.')
        return redirect('login')

    # Get the institution_id from the session
    institution_id = request.session['institution_id']

    try:
        # Fetch the institution based on the institution_id from the session
        institution = Institution.objects.get(institution_id=institution_id)
    except Institution.DoesNotExist:
        messages.error(request, "Institution not found.")
        return redirect('login')

    # Fetch all teachers associated with the logged-in institution
    teachers = Teachers.objects.filter(institution_id=institution_id)

    # Handle POST request to add a new teacher
    if request.method == 'POST':
        # Get the form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        class_id = request.POST.get('class')

        # Ensure class is valid
        try:
            teacher_class = Classes.objects.get(id=class_id, institution_id=institution_id)
        except Classes.DoesNotExist:
            messages.error(request, "Invalid class selected.")
            return redirect('admin_teachers')

        try:
            # Create the teacher record inside a transaction to ensure atomicity
            with transaction.atomic():
                # Create the user record (role as 'teacher')
                user_id = Users.objects.create(role='teacher')

                # Create the teacher record, linking to the user and institution
                teacher = Teachers.objects.create(
                    email=email,
                    password=password,  # In plaintext (as per your setup)
                    name=name,
                    class_id=teacher_class,
                    institution_id=institution,  # Link to the institution
                    user_id=user_id  # Link to the user record
                )

            messages.success(request, f'Teacher {teacher.name} added successfully!')
            return redirect('admin_teachers')  # Redirect to update the list
        except IntegrityError:
            messages.error(request, "An error occurred while adding the teacher.")
            return redirect('admin_teachers')

    # Fetch all classes for the logged-in institution
    classes = Classes.objects.filter(institution_id=institution_id)

    # Prepare context for the template
    context = {
        'institution_name': institution.institution_name,
        'teachers': teachers,
        'classes': classes,  # Adding the classes to the context for the dropdown
    }

    # Render the template
    return render(request, 'admin/admin_teachers.html', context)



def admin_students(request):
    # Ensure the user is an admin
    if 'institution_id' not in request.session:
        messages.error(request, "Please log in to access the admin profile.")
        return redirect('login')
    
    # Get the institution_id from the session
    institution_id = request.session['institution_id']
    
    try:
        # Fetch the institution based on the institution_id from the session
        institution = Institution.objects.get(institution_id=institution_id)

        # Current institution details
        institution_name = institution.institution_name
    except Institution.DoesNotExist:
        messages.error(request, "Institution not found.")
        return redirect('login')

    with connection.cursor() as cursor:
        # Fetch all student details with class and teacher data
        cursor.execute("""
            SELECT s.id, s.name AS student_name, c.name AS class_name, t.name AS teacher_name
            FROM main_students s
            LEFT JOIN main_classes c ON s.class_id_id = c.id
            LEFT JOIN main_teachers t ON c.id = t.class_id_id
            WHERE c.institution_id_id = %s
        """, [institution_id])

        students = cursor.fetchall()

    # Create a list of students
    students_list = [{
        'id': row[0],
        'name': row[1],
        'class_name': row[2] if row[2] else "Not Assigned",
        'teacher_name': row[3] if row[3] else "Not Assigned",
    } for row in students] if students else []

    return render(request, 'admin/admin_students.html', {
        'institution_name': institution_name,
        'students': students_list,
        'student_count': len(students_list),
    })


def admin_profile(request):
    # Check if the user is logged in (session variable 'institution_id' is set)
    if 'institution_id' not in request.session:
        messages.error(request, "Please log in to access the admin profile.")
        return redirect('login')

    # Get the institution_id from the session
    institution_id = request.session['institution_id']
    
    try:
        # Fetch the institution based on the institution_id from the session
        institution = Institution.objects.get(institution_id=institution_id)

        # Current institution details
        institution_name = institution.institution_name
        password = institution.password
        email = institution.email
    except Institution.DoesNotExist:
        messages.error(request, "Institution not found.")
        return redirect('login')

    # Handle form submission (POST request)
    if request.method == 'POST':
        # Update the institution name and password if they are provided in the form
        new_institution_name = request.POST.get('institution_name')
        new_password = request.POST.get('password')

        # Update the institution details in the database
        if new_institution_name:
            institution.institution_name = new_institution_name
        if new_password:
            institution.password = new_password

        institution.save()  # Save the updated institution details

        messages.success(request, 'Your profile has been updated successfully.')
        return redirect('admin_profile')  # Redirect to prevent re-posting on refresh

    # Render the profile page with the current details
    context = {
        'institution_name': institution_name,
        'password': password,
        'email': email
    }
    
    return render(request, 'admin/admin_profile.html', context)


# Institution Registration
def register_institution(request):
    if request.method == 'POST':
        form = InstitutionRegisterForm(request.POST)
        if form.is_valid():
            institution_name = form.cleaned_data['institution_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Check if the email already exists
            if Institution.objects.filter(email=email).exists():
                form.add_error('email', 'An institution with this email already exists.')
            else:
                try:
                    # Create the institution
                    Institution.objects.create(
                        institution_name=institution_name,
                        email=email,
                        password=password  # Store plain password here
                    )
                    messages.success(request, 'Institution registered successfully! Please log in.')
                    return redirect('login')
                except Exception as e:
                    form.add_error(None, 'An error occurred while saving the data. Please try again.')
    else:
        form = InstitutionRegisterForm()

    return render(request, 'registration/institution_register.html', {'form': form})

# Institution Login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Authenticate the institution  
            try:
                institution = Institution.objects.get(email=email, password=password)

                # Set session variables
                request.session['institution_id'] = institution.institution_id
                request.session['institution_name'] = institution.institution_name

                # Redirect to the admin dashboard
                return redirect('admin_dashboard')  # Adjust the URL name accordingly
            except Institution.DoesNotExist:
                messages.error(request, 'Invalid email or password.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

# Admin Logout
def logout(request):
    # Clear session and logout
    request.session.flush()
    return redirect('/')


def teacher_login_view(request):
    form = TeacherLoginForm()  # Instantiate the form

    if request.method == 'POST':
        form = TeacherLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)

            # Validate credentials
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT t.id FROM main_teachers t
                    JOIN main_users u ON t.user_id_id = u.id
                    WHERE t.email = %s AND t.password = %s AND u.role = 'teacher'
                """, [email, password])
                teacher = cursor.fetchone()

            if teacher:
                request.session['teacher_id'] = teacher[0]
                return redirect('teacher_dashboard')
            else:
                messages.error(request, 'Invalid email or password.')

    return render(request, 'teachers/teacher_login.html', {'form': form})



def teacher_dashboard_view(request):
    teacher_id = request.session.get('teacher_id')
    if not teacher_id:
        return redirect('teacher_login')  # Redirect to login if not logged in
    
    # Fetch the logged-in teacher
    teacher = Teachers.objects.get(id=teacher_id)

    # Ensure the teacher object has a class assigned
    teacher_name = teacher.name  # Assuming the teacher has a 'name' field
    teacher_class = teacher.class_id.name if teacher.class_id else 'No class assigned'  # Adjust if necessary

    # Fetch students for the teacher's class (assuming 'class_id' is a foreign key in Students model)
    students = Students.objects.filter(class_id=teacher.class_id)  # Adjust if necessary
    student_count = students.count()

    # Pass the teacher-specific data to the template
    return render(request, 'teachers/teacher_dashboard.html', {
        'teacher_name': teacher_name,  # Pass the teacher's name
        'teacher_class': teacher_class,  # Pass the teacher's class name
        'student_count': student_count,  # Pass the count of students
    })

def teacher_class(request):
    teacher_id = request.session.get('teacher_id')
    if not teacher_id:
        return redirect('teacher_login')  # Redirect to login if not logged in
    
    # Fetch the logged-in teacher
    teacher = Teachers.objects.get(id=teacher_id)

    # Ensure the teacher object has a class assigned
    teacher_name = teacher.name  # Assuming the teacher has a 'name' field
    teacher_class = teacher.class_id.name if teacher.class_id else 'No class assigned'  # Adjust if necessary

    # Fetch students for the teacher's class (assuming 'class_id' is a foreign key in Students model)
    students = Students.objects.filter(class_id=teacher.class_id)  # Adjust if necessary

    # Get the count of students
    student_count = students.count()
    
    # Pass the teacher-specific data and students to the template
    return render(request, 'teachers/teacher_class.html', {
        'teacher_name': teacher_name,  # Pass the teacher's name
        'teacher_class': teacher_class,  # Pass the teacher's class name
        'students': students,  # Pass the students of the teacher's class
        'student_count': student_count,  # Pass the count of students
    })



def teacher_students(request):
    teacher_id = request.session.get('teacher_id')
    if not teacher_id:
        return redirect('teacher_login')  # Redirect to login if not logged in
    
    # Fetch the logged-in teacher
    teacher = Teachers.objects.get(id=teacher_id)
    
    if request.method == 'POST':
        # Get input data from the form
        roll_no = request.POST.get('roll_no')
        student_name = request.POST.get('name')

        try:
            with transaction.atomic():
                # 1. Add student data to the Users table
                student_user = Users.objects.create(role='student')

                # 2. Add student data to the Students table, with the teacher's class_id
                student = Students.objects.create(
                    roll_no=roll_no,
                    password=roll_no,  # Default password is roll_no
                    user_id_id=student_user.id,
                    class_id_id=teacher.class_id.id,  # Set class_id to the teacher's class
                    name=student_name,
                )

                # 3. Add parent data to the Users table
                parent_user = Users.objects.create(role='parent')

                # 4. Add parent data to the Parents table
                Parents.objects.create(
                    password=roll_no,  # Default password is same as student's roll_no
                    student_roll_no_id=roll_no,
                    user_id_id=parent_user.id,
                )

                messages.success(request, "Student and parent records added successfully!")
                return redirect('teacher_students')  # Redirect to the same page

        except Exception as e:
            messages.error(request, f"Error adding student: {str(e)}")
            return redirect('teacher_students')

    # Fetch all students assigned to the teacher's class
    students = Students.objects.filter(class_id_id=teacher.class_id.id)

    return render(request, 'teachers/teacher_students.html', {
        'students': students,
        'teacher_class': teacher.class_id.name,  # Pass the teacher's class name to the template
        'teacher_class_id': teacher.class_id.id,  # Pass the teacher's class ID to the template
    })

def teacher_profile(request):
    teacher_id = request.session.get('teacher_id')
    if not teacher_id:
        return redirect('teacher_login')  # Redirect to login if not logged in

    # Fetch the teacher along with their institution using 'institution_id'
    teacher = Teachers.objects.get(id=teacher_id)
    institution = teacher.institution_id  # Get the institution using the ForeignKey
    institution_name = institution.institution_name  # Get the institution's name

    if request.method == 'POST':
        teacher.name = request.POST.get('name')
        teacher.password = request.POST.get('password')
        teacher.save()
        messages.success(request, 'Profile updated successfully.')

    return render(request, 'teachers/teacher_profile.html', {
        'teacher': teacher,
        'institution_name': institution_name
    })


def student_login(request):
    form = StudentLoginForm()

    if request.method == "POST":
        form = StudentLoginForm(request.POST)

        if form.is_valid():
            roll_no = form.cleaned_data.get("roll_no")
            password = form.cleaned_data.get("password")

            # Validate credentials with raw SQL query
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT s.id FROM main_students s
                    JOIN main_users u ON s.user_id_id = u.id
                    WHERE s.roll_no = %s AND s.password = %s AND u.role = 'student'
                """, [roll_no, password])
                student = cursor.fetchone()

            if student:
                request.session['student_id'] = student[0]  # Save student ID in session
                return redirect('student_dashboard')
            else:
                messages.error(request, 'Invalid roll number or password.')

    return render(request, 'students/student_login.html', {'form': form})


def student_dashboard(request):
    # Ensure the student is logged in
    if 'student_id' not in request.session:
        return redirect('student_login')

    student_id = request.session['student_id']

    with connection.cursor() as cursor:
        # Fetch the student's name and class ID
        cursor.execute("""
            SELECT s.name, s.class_id_id 
            FROM main_students s 
            WHERE s.id = %s
        """, [student_id])
        student_data = cursor.fetchone()

        if not student_data:
            return redirect('student_login')  # Redirect if student data is invalid

        student_name, class_id = student_data

        teacher_name = None
        teacher_class = None

        if class_id:  # If the student is assigned to a class
            # Fetch the teacher's name and class name based on the class ID
            cursor.execute("""
                SELECT t.name, c.name
                FROM main_teachers t
                JOIN main_classes c ON t.class_id_id = c.id
                WHERE c.id = %s
            """, [class_id])
            teacher_data = cursor.fetchone()

            if teacher_data:
                teacher_name, teacher_class = teacher_data

    # Pass data to the template
    return render(request, 'students/student_dashboard.html', {
        'student_name': student_name,
        'teacher_name': teacher_name if teacher_name else "Not Assigned",
        'teacher_class': teacher_class if teacher_class else "Not Assigned",
    })


def student_profile(request):
    # Ensure the student is logged in
    if 'student_id' not in request.session:
        return redirect('student_login')

    student_id = request.session['student_id']

    if request.method == 'POST':
        # Handle the form submission and update the student details
        name = request.POST.get('name')
        password = request.POST.get('password')

        with connection.cursor() as cursor:
            # Update student profile in the database
            cursor.execute("""
                UPDATE main_students
                SET name = %s
                WHERE id = %s
            """, [name, student_id])

            if password:  # Only update password if a new one is provided
                cursor.execute("""
                    UPDATE main_students
                    SET password = %s
                    WHERE id = %s
                """, [password, student_id])

        # Redirect after updating the profile
        return redirect('student_profile')

    with connection.cursor() as cursor:
        # Fetch student profile data including current password
        cursor.execute("""
            SELECT s.name, s.roll_no, c.name as class_name, t.name as teacher_name, t.email as teacher_email, i.institution_name as institution_name, s.password
            FROM main_students s
            LEFT JOIN main_classes c ON s.class_id_id = c.id
            LEFT JOIN main_teachers t ON c.id = t.class_id_id
            LEFT JOIN main_institution i ON c.institution_id_id = i.institution_id
            WHERE s.id = %s
        """, [student_id])
        profile_data = cursor.fetchone()

    # If student data is missing (edge case), redirect to login
    if not profile_data:
        return redirect('student_login')

    student_name, roll_no, class_name, teacher_name, teacher_email, institution_name, current_password = profile_data

    return render(request, 'students/student_profile.html', {
        'student_name': student_name,
        'roll_no': roll_no,
        'class_name': class_name if class_name else "Not Assigned",
        'teacher_name': teacher_name if teacher_name else "Not Assigned",
        'teacher_email': teacher_email if teacher_email else "Not Assigned",
        'institution_name': institution_name if institution_name else "Not Assigned",
        'current_password': current_password,
    })


def student_class(request):
    # Ensure the student is logged in
    if 'student_id' not in request.session:
        return redirect('student_login')

    student_id = request.session['student_id']

    with connection.cursor() as cursor:
        # Fetch student details
        cursor.execute("""
            SELECT s.name AS student_name, c.name AS class_name, t.name AS teacher_name
            FROM main_students s
            LEFT JOIN main_classes c ON s.class_id_id = c.id
            LEFT JOIN main_teachers t ON c.id = t.class_id_id
            WHERE s.id = %s
        """, [student_id])
        student_details = cursor.fetchone()

        # Fetch list of students in the same class
        cursor.execute("""
            SELECT s.roll_no, s.name
            FROM main_students s
            WHERE s.class_id_id = (
                SELECT class_id_id
                FROM main_students
                WHERE id = %s
            )
        """, [student_id])
        students = cursor.fetchall()

    # Handle edge cases where student or class data is missing
    if not student_details:
        student_name, class_name, teacher_name = "Unknown", "Not Assigned", "Not Assigned"
    else:
        student_name, class_name, teacher_name = student_details

    students_list = [{'roll_no': row[0], 'name': row[1]} for row in students] if students else []

    return render(request, 'students/student_class.html', {
        'student_name': student_name,
        'class_name': class_name,
        'teacher_name': teacher_name,
        'teacher_class': class_name if class_name else "Not Assigned",
        'students': students_list,
        'student_count': len(students_list),
    })


def parent_login(request):
    form = ParentLoginForm()

    if request.method == "POST":
        form = ParentLoginForm(request.POST)

        if form.is_valid():
            roll_no = form.cleaned_data.get("roll_no")
            password = form.cleaned_data.get("password")

            # Validate credentials with raw SQL query
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT p.id FROM main_parents p
                    JOIN main_users u ON p.user_id_id = u.id
                    WHERE p.student_roll_no_id = %s AND p.password = %s AND u.role = 'parent'
                """, [roll_no, password])
                parent = cursor.fetchone()

            if parent:
                # Save the parent ID in session (for use in dashboard or elsewhere)
                request.session['parent_id'] = parent[0]
                messages.success(request, "Login successful.")
                return redirect('parent_dashboard')  # Replace with the actual parent dashboard route
            else:
                messages.error(request, "Invalid roll number or password.")

    return render(request, 'parents/parent_login.html', {'form': form})


def parent_dashboard(request):
    # Ensure the parent is logged in
    parent_id = request.session.get('parent_id')
    if not parent_id:
        return redirect('parent_login')  # Redirect to the login page if not logged in

    with connection.cursor() as cursor:
        # Fetch parent and associated student details
        cursor.execute("""
            SELECT p.id, p.name AS parent_name, p.student_roll_no_id, 
                   s.name AS student_name, s.class_id_id
            FROM main_parents p
            JOIN main_students s ON p.student_roll_no_id = s.roll_no
            WHERE p.id = %s
        """, [parent_id])
        parent_data = cursor.fetchone()

        # Redirect to login if parent or student data is missing
        if not parent_data:
            return redirect('parent_login')

        # Extract details
        parent_id = parent_data[0]
        parent_name = parent_data[1]
        student_roll_no = parent_data[2]
        student_name = parent_data[3]
        student_class_id = parent_data[4]

        # Fetch class name
        cursor.execute("""
            SELECT name FROM main_classes
            WHERE id = %s
        """, [student_class_id])
        class_data = cursor.fetchone()
        student_class = class_data[0] if class_data else "Class not assigned"

        # Fetch class teacher's name
        cursor.execute("""
            SELECT t.name 
            FROM main_teachers t
            WHERE t.class_id_id = %s
        """, [student_class_id])
        teacher_data = cursor.fetchone()
        class_teacher = teacher_data[0] if teacher_data else "No teacher assigned"

    # Prepare context for the template
    context = {
        'parent_id': parent_id,
        'parent_name': parent_name,
        'student_roll_no': student_roll_no,
        'student_name': student_name,
        'student_class': student_class,
        'class_teacher': class_teacher,
    }

    return render(request, 'parents/parent_dashboard.html', context)



def parent_teacher_profile(request):
    parent_id = request.session.get('parent_id')  # Ensure the parent is logged in
    if not parent_id:
        return redirect('parent_login')

    # Fetch teacher details associated with the parent's student
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT t.name AS teacher_name, t.email AS teacher_email, 
                   c.name AS class_name, i.institution_name
            FROM main_parents p
            JOIN main_students s ON p.student_roll_no_id = s.roll_no
            LEFT JOIN main_classes c ON s.class_id_id = c.id
            LEFT JOIN main_teachers t ON c.id = t.class_id_id
            LEFT JOIN main_institution i ON t.institution_id_id = i.institution_id
            WHERE p.id = %s
        """, [parent_id])
        teacher_data = cursor.fetchone()

    # Handle case where teacher data is not found
    if not teacher_data:
        messages.error(request, "Unable to retrieve teacher details.")
        return redirect('parent_dashboard')

    # Prepare context data for the template
    context = {
        'teacher_name': teacher_data[0] or "N/A",
        'teacher_email': teacher_data[1] or "N/A",
        'class_name': teacher_data[2] or "N/A",
        'institution_name': teacher_data[3] or "N/A",
    }
    return render(request, 'parents/parent_teacher_profile.html', context)



def parent_profile(request):
    parent_id = request.session.get('parent_id')  # Ensure the parent is logged in
    if not parent_id:
        return redirect('parent_login')

    if request.method == 'POST':
        # Handle profile update
        parent_name = request.POST.get('parent_name')
        password = request.POST.get('password')

        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE main_parents 
                SET name = %s, password = %s 
                WHERE id = %s
            """, [parent_name, password, parent_id])
            messages.success(request, "Profile updated successfully!")
        return redirect('parent_profile')

    # Fetch parent's profile details
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT p.name AS parent_name, p.password, 
                   s.name AS student_name, s.roll_no, 
                   c.name AS class_name, 
                   t.name AS teacher_name, t.email AS teacher_email
            FROM main_parents p
            JOIN main_students s ON p.student_roll_no_id = s.roll_no
            LEFT JOIN main_classes c ON s.class_id_id = c.id
            LEFT JOIN main_teachers t ON c.id = t.class_id_id
            WHERE p.id = %s
        """, [parent_id])
        parent_data = cursor.fetchone()

    # Handle case where profile data is not found
    if not parent_data:
        messages.error(request, "Unable to retrieve profile details.")
        return redirect('parent_dashboard')

    # Prepare context data for the template
    context = {
        'parent_name': parent_data[0] or "",
        'password': parent_data[1] or "",
        'student_name': parent_data[2] or "N/A",
        'student_roll_no': parent_data[3] or "N/A",
        'class_name': parent_data[4] or "N/A",
        'teacher_name': parent_data[5] or "N/A",
        'teacher_email': parent_data[6] or "N/A",
    }
    return render(request, 'parents/parent_profile.html', context)


