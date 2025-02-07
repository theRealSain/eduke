from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import InstitutionRegisterForm, LoginForm, ClassHeadLoginForm, SubjectHeadLoginForm, StudentLoginForm, ParentLoginForm, AddClassForm, AddSubjectForm
from .models import Institution, Classes, Subjects, Students, Users, Parents, Chat
from django.db import IntegrityError, transaction
from django.db import connection
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.timezone import now


# Index page
def index(request):
    return render(request, 'index.html')


######################################################################################################################


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

######################################################################################################################

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
    
    # Calculate the total number of users (class heads + students)
    total_users = Users.objects.filter(
        id__in=Classes.objects.filter(institution_id=institution_id).values('user')
    ).count() + Users.objects.filter(
        id__in=Students.objects.filter(class_obj__in=Classes.objects.filter(institution_id=institution_id).values('id')).values('user')
    ).count()

    # Get all classes belonging to the logged-in institution
    total_classes = Classes.objects.filter(institution_id=institution_id).count()

    # Count the students belonging to those classes
    student_count = Students.objects.filter(
        class_obj__in=Classes.objects.filter(institution_id=institution_id).values('id')
    ).count()

    # Pass the counts to the template
    context = {
        'institution_name': institution_name,
        'total_users': total_users,
        'student_count': student_count,
        'total_classes': total_classes,
    }

    return render(request, 'admin/admin_dashboard.html', context)


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
            # Start a transaction to ensure atomicity
            with transaction.atomic():
                # Get the values from the form
                class_name = form.cleaned_data['class_name']
                class_head = form.cleaned_data['class_head']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']

                # Create a new user for the class head
                user = Users.objects.create(
                    role='class_head',  # Set the role as 'class_head'
                )

                # Create the new class and associate it with the institution and the created user
                new_class = Classes(
                    class_name=class_name,
                    class_head=class_head,  # Class head's name
                    email=email,
                    password=password,
                    institution=institution,  # Set institution from the session
                    user=user  # Link the newly created user
                )
                new_class.save()  # Save the new class record

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


######################################################################################################################


def class_head_login(request):
    form = ClassHeadLoginForm()

    if request.method == 'POST':
        form = ClassHeadLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Fetch class head record
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT c.id, c.password, u.role
                    FROM main_classes c
                    JOIN main_users u ON c.user_id = u.id
                    WHERE c.email = %s
                """, [email])

                class_head = cursor.fetchone()

            if class_head:
                class_id, db_password, role = class_head

                # Validate role and password
                if role == 'class_head' and db_password == password:
                    request.session['class_id'] = class_id  # Store class_id in session
                    return redirect('class_head_dashboard')  # Redirect to the dashboard
                else:
                    messages.error(request, 'Invalid credentials or access restricted.')
            else:
                messages.error(request, 'No Class Head found with this email.')

    return render(request, 'class_head/class_head_login.html', {'form': form})



def class_head_dashboard(request):
    class_id = request.session.get('class_id')

    # If no class_id in session, redirect to login
    if not class_id:
        messages.error(request, 'Session expired or not logged in. Please log in again.')
        return redirect('class_head_login')

    # Fetch class details for the logged-in class head
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT c.class_name, c.email, c.class_head
            FROM main_classes c
            WHERE c.id = %s
        """, [class_id])
        class_details = cursor.fetchone()

    # Ensure class_details is not None
    if not class_details:
        messages.error(request, 'Class details not found.')
        return redirect('class_head_login')

    # Fetch student count
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT COUNT(*)
            FROM main_students s
            WHERE s.class_obj_id = %s
        """, [class_id])
        student_count = cursor.fetchone()[0]  # Fetch count of students in this class

    # Fetch subject count
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT COUNT(*)
            FROM main_subjects sub
            WHERE sub.class_obj_id = %s
        """, [class_id])
        subject_count = cursor.fetchone()[0]  # Fetch count of subjects for this class

    return render(request, 'class_head/class_head_dashboard.html', {
        'class_details': class_details,
        'student_count': student_count,
        'subject_count': subject_count,  # Add subject count to template context
    })


def class_head_class(request):
    class_id = request.session.get('class_id')
    if not class_id:
        return redirect('class_head_login')  # Redirect to login if not logged in
    
    # Fetch the class details for the logged-in class head
    try:
        class_details = Classes.objects.get(id=class_id)  # Retrieve class using the class_id
    except Classes.DoesNotExist:
        messages.error(request, 'Class not found.')
        return redirect('class_head_login')

    # Ensure the class head is assigned
    class_head_name = class_details.class_head  # The class head's name is stored in the class_head field
    class_name = class_details.class_name  # The class name

    # Fetch subjects linked to the class
    subjects = Subjects.objects.filter(class_obj=class_details)  # Fetch all subjects for the class
    subject_count = subjects.count()  # Count the number of subjects

    # Fetch students for the class (assuming 'class_obj' is a foreign key in the Students model)
    students = Students.objects.filter(class_obj=class_details)  # Adjust if necessary

    # Get the count of students
    student_count = students.count()

    # Pass the class head-specific data, subjects, and students to the template
    return render(request, 'class_head/class_head_class.html', {
        'class_head_name': class_head_name,  # Pass the class head's name
        'class_name': class_name,  # Pass the class name
        'students': students,  # Pass the students of the class
        'student_count': student_count,  # Pass the count of students
        'subjects': subjects,  # Pass the subjects of the class
    })


def class_head_students(request):
    class_id = request.session.get('class_id')
    if not class_id:
        return redirect('class_head_login')  # Redirect to login if not logged in
    
    # Fetch the class details for the logged-in class head
    try:
        class_details = Classes.objects.get(id=class_id)  # Retrieve class using the class_id
    except Classes.DoesNotExist:
        messages.error(request, 'Class not found.')
        return redirect('class_head_login')

    # Fetch all students assigned to this class
    students = Students.objects.filter(class_obj=class_details)

    if request.method == 'POST':
        # Get input data from the form
        roll_no = request.POST.get('roll_no')
        student_name = request.POST.get('name')

        # Validate input fields
        if not roll_no or not student_name:
            messages.error(request, "Roll number and name are required.")
            return redirect('class_head_students')

        try:
            with transaction.atomic():
                # 1. Add student data to the Users table
                student_user = Users.objects.create(role='student')

                # 2. Add student data to the Students table, with the class_id from the logged-in class
                student = Students.objects.create(
                    roll_no=roll_no,
                    password=roll_no,  # Default password is roll_no
                    user=student_user,  # Link the user_id to the student user created above
                    class_obj=class_details,  # Set class_obj to the logged-in class
                    name=student_name,
                )

                # 3. Add parent data to the Users table
                parent_user = Users.objects.create(role='parent')

                # 4. Add parent data to the Parents table, associating the parent with the student
                Parents.objects.create(
                    password=roll_no,  # Default password is same as student's roll_no
                    student=student,  # Link the parent to the created student
                    user=parent_user,  # Link the user_id to the parent user created above
                )

                messages.success(request, "Student and parent records added successfully!")
                return redirect('class_head_students')  # Redirect to the same page to refresh

        except Exception as e:
            messages.error(request, f"Error adding student and parent: {str(e)}")
            return redirect('class_head_students')

    # Render the page with student data and the class details
    return render(request, 'class_head/class_head_students.html', {
        'students': students,
        'class_name': class_details.class_name,  # Pass the class name to the template
        'class_id': class_details.id,  # Pass the class ID to the template
    })


def class_head_subjects(request):
    class_id = request.session.get('class_id')
    if not class_id:
        return redirect('class_head_login')  # Redirect to login if not logged in

    try:
        class_details = Classes.objects.get(id=class_id)
        subjects = Subjects.objects.filter(class_obj=class_details)  # Fetch subjects for the class
    except Classes.DoesNotExist:
        messages.error(request, 'Class not found.')
        return redirect('class_head_login')

    if request.method == 'POST':
        form = AddSubjectForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    subject_name = form.cleaned_data['subject_name']
                    subject_head = form.cleaned_data['subject_head']
                    email = form.cleaned_data['email']
                    password = form.cleaned_data['password']

                    user = Users.objects.create(role='subject_head')

                    subject = Subjects.objects.create(
                        subject_name=subject_name,
                        subject_head=subject_head,
                        email=email,
                        password=password,
                        user=user,
                        class_obj=class_details
                    )

                messages.success(request, "Subject added successfully!")
                return redirect('class_head_subjects')
            except Exception as e:
                messages.error(request, f"Error adding subject: {str(e)}")
        else:
            messages.error(request, "Invalid input. Please check the form.")

    else:
        form = AddSubjectForm()

    return render(request, 'class_head/class_head_subjects.html', {
        'class_name': class_details.class_name,
        'class_id': class_id,
        'form': form,
        'subjects': subjects,  # Pass subjects to the template
    })


def class_head_profile(request):
    class_head_id = request.session.get('class_id')  # Use the correct session key
    
    if not class_head_id:
        return redirect('class_head_login')  # Redirect if not logged in

    # Fetch the class (which represents the class head) along with its institution
    class_head = get_object_or_404(Classes, id=class_head_id)
    
    # Get institution object using the foreign key relationship (assuming it's a ForeignKey)
    institution = class_head.institution_id  # This is the integer (ID) for institution

    if institution:
        # Fetch the institution object to get the institution_name
        institution_obj = get_object_or_404(Institution, institution_id=institution)
        institution_name = institution_obj.institution_name
    else:
        institution_name = "Unknown Institution"

    if request.method == 'POST':
        class_head.class_head = request.POST.get('name')  # Update class head name
        password = request.POST.get('password')
        if password:  # Only update password if provided
            class_head.password = password
        class_head.save()
        messages.success(request, 'Profile updated successfully.')

    return render(request, 'class_head/class_head_profile.html', {
        'class_head': class_head,
        'institution_name': institution_name
    })



def class_head_chat(request):
    # Retrieve the class_id from session
    class_id = request.session.get('class_id')

    # If class_id is not found in session, redirect to login
    if not class_id:
        return redirect('class_head_login')

    # Retrieve the class head using the class_id
    class_head = Classes.objects.get(id=class_id)
    class_head_user = class_head.user  # Fetch the associated user for the class head

    # Fetch distinct users (subject heads, students, and parents) who can message the logged-in class head
    with connection.cursor() as cursor:
        cursor.execute(""" 
            SELECT DISTINCT u.id, u.role, 
                   CASE
                       WHEN u.role = 'subject_head' THEN s.subject_head
                       WHEN u.role = 'student' THEN st.name
                       WHEN u.role = 'parent' THEN 
                           CASE
                               WHEN p.student_id IS NOT NULL THEN 
                                   (SELECT st.name FROM main_students AS st WHERE st.roll_no = p.student_id)
                               ELSE p.name
                           END
                   END AS user_name
            FROM main_chat AS chat
            JOIN main_users AS u ON (chat.sender_id = u.id OR chat.receiver_id = u.id)
            LEFT JOIN main_subjects AS s ON s.user_id = u.id AND u.role = 'subject_head'
            LEFT JOIN main_students AS st ON st.user_id = u.id AND u.role = 'student'
            LEFT JOIN main_parents AS p ON p.user_id = u.id AND u.role = 'parent'
            WHERE (chat.sender_id = %s OR chat.receiver_id = %s)
            AND u.role != 'class_head'
            ORDER BY user_name;
        """, [class_head_user.id, class_head_user.id])

        involved_users = cursor.fetchall()

        # Debug print to check the data structure
        print("Involved Users:", involved_users)

        # Fetch all students, parents, and subject heads for the class
        cursor.execute("""
            SELECT u.id, u.role, 
                   CASE
                       WHEN u.role = 'subject_head' THEN s.subject_head
                       WHEN u.role = 'student' THEN st.name
                       WHEN u.role = 'parent' THEN 
                           CASE
                               WHEN p.student_id IS NOT NULL THEN 
                                   (SELECT st.name FROM main_students AS st WHERE st.roll_no = p.student_id)
                               ELSE p.name
                           END
                   END AS user_name
            FROM main_users AS u
            LEFT JOIN main_subjects AS s ON s.user_id = u.id AND u.role = 'subject_head'
            LEFT JOIN main_students AS st ON st.user_id = u.id AND u.role = 'student'
            LEFT JOIN main_parents AS p ON p.user_id = u.id AND u.role = 'parent'
            WHERE u.role IN ('subject_head', 'student', 'parent')
            AND (
                st.class_obj_id = %s OR 
                p.student_id IN (SELECT roll_no FROM main_students WHERE class_obj_id = %s) OR
                s.class_obj_id = %s
            )
            ORDER BY user_name;
        """, [class_id, class_id, class_id])

        all_users_for_class = cursor.fetchall()

        # Debug print to check the data structure
        print("All Users for Class:", all_users_for_class)

    # Add users to context for rendering
    context = {
        'class_head': class_head,
        'involved_users': involved_users,
        'all_users_for_class': all_users_for_class,  # New section for class heads to send messages
    }

    return render(request, "class_head/class_head_chat.html", context)



def class_head_chat_user(request, user_id):
    # Retrieve the logged-in class head's ID from session
    class_head_id = request.session.get('class_id')
    if not class_head_id:
        return redirect('class_head_login')

    # Fetch the actual user_id from main_users table based on the session user_id (class_head_id)
    with connection.cursor() as cursor:
        cursor.execute("SELECT user_id FROM main_classes WHERE id = %s", [class_head_id])
        logged_in_user = cursor.fetchone()
        if logged_in_user:
            logged_in_user_id = logged_in_user[0]  # Corrected user ID
            print(f"Logged-in User ID: {logged_in_user_id}")

    # Initialize the user name and role
    selected_user_name = None
    selected_user_role = None

    # Fetch the selected user's name and role
    with connection.cursor() as cursor:
        cursor.execute("SELECT name FROM main_students WHERE user_id = %s", [user_id])
        student_name = cursor.fetchone()
        if student_name:
            selected_user_name = student_name[0]
            selected_user_role = 'Student'
        else:
            cursor.execute("SELECT student_id FROM main_parents WHERE user_id = %s", [user_id])
            parent_student_roll_no = cursor.fetchone()
            if parent_student_roll_no:
                cursor.execute("SELECT name FROM main_students WHERE roll_no = %s", [parent_student_roll_no[0]])
                student_name_for_parent = cursor.fetchone()
                if student_name_for_parent:
                    selected_user_name = f"Parent of {student_name_for_parent[0]}"
                    selected_user_role = 'Parent'
            else:
                cursor.execute("SELECT subject_head FROM main_subjects WHERE user_id = %s", [user_id])
                subject_head_name = cursor.fetchone()
                if subject_head_name:
                    selected_user_name = subject_head_name[0]
                    selected_user_role = 'Subject Head'
                else:
                    cursor.execute("SELECT role FROM main_users WHERE id = %s", [user_id])
                    selected_user = cursor.fetchone()
                    selected_user_role = selected_user[0] if selected_user else 'Unknown'
                    selected_user_name = selected_user_role.capitalize()

    print(f"Chatting with {selected_user_name} ({selected_user_role})")

    # Fetch messages between logged-in user and selected user
    with connection.cursor() as cursor:
        cursor.execute(""" 
            SELECT message, sender_id, receiver_id, created_at 
            FROM main_chat 
            WHERE (sender_id = %s AND receiver_id = %s) 
            OR (sender_id = %s AND receiver_id = %s) 
            ORDER BY created_at;
        """, [user_id, logged_in_user_id, logged_in_user_id, user_id])  
        messages = cursor.fetchall()

    print(f"Messages fetched between {logged_in_user_id} and {user_id}")

    # Handle message sending
    if request.method == 'POST':
        message_text = request.POST.get('message')
        if message_text.strip():  # Ensure message is not empty
            with connection.cursor() as cursor:
                cursor.execute(""" 
                    INSERT INTO main_chat (sender_id, receiver_id, message, created_at) 
                    VALUES (%s, %s, %s, NOW());
                """, [logged_in_user_id, user_id, message_text])
            print(f"Message sent: '{message_text}' from {logged_in_user_id} to {user_id}")
            return redirect('class_head_chat_user', user_id=user_id)  # Refresh page after sending

    context = {
        'selected_user_name': selected_user_name,
        'selected_user_role': selected_user_role,
        'messages': messages,
        'logged_in_user_id': logged_in_user_id,  # Pass correct sender ID
    }
    return render(request, 'class_head/class_head_chat_user.html', context)




######################################################################################################################


def subject_head_login(request):
    form = SubjectHeadLoginForm()

    if request.method == 'POST':
        form = SubjectHeadLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Fetch subject head record
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT s.id, s.password, u.role
                    FROM main_subjects s
                    JOIN main_users u ON s.user_id = u.id
                    WHERE s.email = %s
                """, [email])

                subject_head = cursor.fetchone()

            if subject_head:
                subject_id, db_password, role = subject_head

                # Validate role and password
                if role == 'subject_head' and db_password == password:
                    request.session['subject_id'] = subject_id  # Store subject_id in session
                    return redirect('subject_head_dashboard')  # Redirect to subject head dashboard
                else:
                    messages.error(request, 'Invalid credentials or access restricted.')
            else:
                messages.error(request, 'No Subject Head found with this email.')

    return render(request, 'subject_head/subject_head_login.html', {'form': form})


def subject_head_dashboard(request):
    # Ensure subject head is logged in
    subject_id = request.session.get('subject_id')
    if not subject_id:
        return redirect('subject_head_login')  # Redirect to login page if not logged in

    # Fetch subject details
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT s.subject_name, s.subject_head, c.class_name, c.class_head
            FROM main_subjects s
            JOIN main_classes c ON s.class_obj_id = c.id
            WHERE s.id = %s
        """, [subject_id])

        subject_details = cursor.fetchone()  # Fetch one record

    # Prepare context for the template
    context = {
        'subject_name': subject_details[0] if subject_details else None,
        'subject_head': subject_details[1] if subject_details else None,
        'class_name': subject_details[2] if subject_details else None,
        'class_head': subject_details[3] if subject_details else None,
    }

    return render(request, 'subject_head/subject_head_dashboard.html', context)


def subject_head_class(request):
    # Ensure subject head is logged in
    subject_id = request.session.get('subject_id')
    if not subject_id:
        return redirect('subject_head_login')

    # Fetch class and faculty details
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT c.class_name, c.class_head
            FROM main_subjects s
            JOIN main_classes c ON s.class_obj_id = c.id
            WHERE s.id = %s
        """, [subject_id])
        class_info = cursor.fetchone()

    if class_info:
        class_name, class_head_name = class_info
    else:
        class_name, class_head_name = "Unknown", "Unknown"

    # Fetch the logged-in subject's details
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT subject_name, subject_head, email
            FROM main_subjects
            WHERE id = %s
        """, [subject_id])
        logged_in_subject = cursor.fetchone()

    if logged_in_subject:
        logged_in_subject_name, logged_in_subject_head, logged_in_subject_email = logged_in_subject
    else:
        logged_in_subject_name, logged_in_subject_head, logged_in_subject_email = "Unknown", "Unknown", "Unknown"

    # Fetch subjects under this class
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, subject_name, subject_head, email
            FROM main_subjects
            WHERE class_obj_id = (SELECT class_obj_id FROM main_subjects WHERE id = %s)
        """, [subject_id])
        subjects = [
            {
                'id': row[0],
                'subject_name': row[1],
                'subject_head': row[2],
                'email': row[3],
                'is_logged_in_subject': row[2] == logged_in_subject_head  # Check if the subject belongs to the logged-in user
            }
            for row in cursor.fetchall()
        ]

    # Fetch students under this class
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT roll_no, name
            FROM main_students
            WHERE class_obj_id = (SELECT class_obj_id FROM main_subjects WHERE id = %s)
        """, [subject_id])
        students = [
            {'roll_no': row[0], 'name': row[1]}
            for row in cursor.fetchall()
        ]

    # Get student count
    student_count = len(students)

    context = {
        'class_name': class_name,
        'class_head_name': class_head_name,
        'subjects': subjects,
        'students': students,
        'student_count': student_count,
        'logged_in_subject_head': logged_in_subject_head  # Pass the logged-in subject head to the template
    }

    return render(request, 'subject_head/subject_head_class.html', context)



def subject_head_subjects(request):
    # Ensure subject head is logged in
    subject_id = request.session.get('subject_id')
    if not subject_id:
        return redirect('subject_head_login')

    # Fetch class and faculty details (for the subject head)
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT c.class_name, s.subject_head
            FROM main_subjects s
            JOIN main_classes c ON s.class_obj_id = c.id
            WHERE s.id = %s
        """, [subject_id])
        class_info = cursor.fetchone()

    if class_info:
        class_name, subject_head = class_info
    else:
        class_name, subject_head = "Unknown", "Unknown"

    # Fetch assigned subject details for the specific subject head
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, subject_name, subject_head, email
            FROM main_subjects
            WHERE id = %s
        """, [subject_id])
        subjects = [
            {'id': row[0], 'subject_name': row[1], 'subject_head': row[2], 'email': row[3]}
            for row in cursor.fetchall()
        ]

    # Fetch students under this subject's class
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT roll_no, name
            FROM main_students
            WHERE class_obj_id = (SELECT class_obj_id FROM main_subjects WHERE id = %s)
        """, [subject_id])
        students = [
            {'roll_no': row[0], 'name': row[1]}
            for row in cursor.fetchall()
        ]

    # Get student count
    student_count = len(students)

    context = {
        'class_name': class_name,
        'subject_head': subject_head,  # Pass subject head information to the template
        'subjects': subjects,
        'students': students,
        'student_count': student_count
    }

    return render(request, 'subject_head/subject_head_subjects.html', context)


def subject_head_profile(request):
    # Ensure subject head is logged in
    subject_id = request.session.get('subject_id')
    if not subject_id:
        return redirect('subject_head_login') 

    if request.method == 'POST':
        # Get updated data from the form
        updated_name = request.POST.get('name')
        updated_password = request.POST.get('password')

        # Update the subject head's details in the database
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE main_subjects
                SET subject_head = %s, password = %s
                WHERE id = %s
            """, [updated_name, updated_password, subject_id])
        
        messages.success(request, "Profile updated successfully!")

        return redirect('subject_head_profile')  # Refresh the page after update

    # Fetch current subject head details
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT s.subject_name, s.subject_head, s.email, s.password, c.class_name, c.class_head, i.institution_name
            FROM main_subjects s
            JOIN main_classes c ON s.class_obj_id = c.id
            JOIN main_institution i ON c.institution_id = i.institution_id
            WHERE s.id = %s
        """, [subject_id])

        subject_head = cursor.fetchone()  # Fetch one record

    if subject_head:
        context = {
            'class_head': {
                'subject_name': subject_head[0],  # Subject Name
                'class_head': subject_head[1],  # Subject Head Name
                'email': subject_head[2],
                'password': subject_head[3],
                'class_name': subject_head[4],
            },
            'institution_name': subject_head[6]
        }
    else:
        context = {'class_head': None, 'institution_name': None}

    return render(request, 'subject_head/subject_head_profile.html', context)



def subject_head_chat(request):
    # Ensure subject head is logged in
    subject_id = request.session.get('subject_id')
    if not subject_id:
        print("DEBUG: No subject_id found in session. Redirecting to login.")
        return redirect('subject_head_login')

    print(f"DEBUG: Logged in subject_id: {subject_id}")

    # Fetch user_id and class_id for the logged-in subject head
    with connection.cursor() as cursor:
        cursor.execute("SELECT user_id, class_obj_id FROM main_subjects WHERE id = %s", [subject_id])
        subject_data = cursor.fetchone()

    if not subject_data:
        print(f"DEBUG: No user data found for subject_id {subject_id}.")
        return redirect('subject_head_login')

    subject_user_id, class_id = subject_data
    print(f"DEBUG: Retrieved subject_user_id: {subject_user_id}, class_obj_id: {class_id}")

    # Fetch users involved in chat
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT u.id, u.role, 
            COALESCE(
                c.class_head, 
                s.subject_head, 
                st.name, 
                CASE 
                    WHEN p.user_id IS NOT NULL THEN CONCAT('Parent of ', st2.name) 
                    ELSE NULL 
                END
            ) AS name
        FROM main_users u
        LEFT JOIN main_classes c ON u.id = c.user_id AND u.role = 'class_head'
        LEFT JOIN main_subjects s ON u.id = s.user_id AND u.role = 'subject_head'
        LEFT JOIN main_students st ON u.id = st.user_id AND u.role = 'student'
        LEFT JOIN main_parents p ON u.id = p.user_id AND u.role = 'parent'
        LEFT JOIN main_students st2 ON p.student_id = st2.roll_no AND u.role = 'parent'
        WHERE u.id IN (
            SELECT DISTINCT sender_id FROM main_chat WHERE receiver_id = %s
            UNION
            SELECT DISTINCT receiver_id FROM main_chat WHERE sender_id = %s
        );
        """, [subject_user_id, subject_user_id])

        chat_users = [{'id': row[0], 'role': row[1], 'name': row[2] or 'Unknown'} for row in cursor.fetchall()]

    print(f"DEBUG: Retrieved users involved in chat: {chat_users}")

    # Fetch users the subject head can send messages to (students, parents, class head, other subject heads)
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT u.id, u.role, 
            COALESCE(
                st.name, 
                CASE 
                    WHEN p.user_id IS NOT NULL THEN CONCAT('Parent of ', st2.name) 
                    ELSE NULL 
                END,
                c.class_head,
                s.subject_head
            ) AS name
        FROM main_users u
        LEFT JOIN main_students st ON u.id = st.user_id AND u.role = 'student' AND st.class_obj_id = %s
        LEFT JOIN main_parents p ON u.id = p.user_id AND u.role = 'parent'
        LEFT JOIN main_students st2 ON p.student_id = st2.roll_no AND u.role = 'parent' AND st2.class_obj_id = %s
        LEFT JOIN main_classes c ON u.id = c.user_id AND u.role = 'class_head' AND c.id = %s
        LEFT JOIN main_subjects s ON u.id = s.user_id AND u.role = 'subject_head' AND s.class_obj_id = %s
        WHERE (st.class_obj_id IS NOT NULL OR st2.class_obj_id IS NOT NULL OR c.id IS NOT NULL OR (s.class_obj_id IS NOT NULL AND u.id != %s));
        """, [class_id, class_id, class_id, class_id, subject_user_id])

        message_users = [{'id': row[0], 'role': row[1], 'name': row[2] or 'Unknown'} for row in cursor.fetchall()]

    print(f"DEBUG: Retrieved users the subject head can send messages to: {message_users}")

    return render(request, 'subject_head/subject_head_chat.html', {'chat_users': chat_users, 'message_users': message_users})



def subject_head_chat_user(request, user_id):
    # Ensure subject head is logged in
    subject_id = request.session.get('subject_id')
    if not subject_id:
        print("DEBUG: No subject_id found in session. Redirecting to login.")
        return redirect('subject_head_login')

    print(f"DEBUG: Logged in subject_id: {subject_id}")

    # Fetch user_id for the logged-in subject head
    with connection.cursor() as cursor:
        cursor.execute("SELECT user_id FROM main_subjects WHERE id = %s", [subject_id])
        subject_user_id = cursor.fetchone()

    if not subject_user_id:
        print(f"DEBUG: No user_id found for subject_id {subject_id}. Redirecting to login.")
        return redirect('subject_head_login')

    subject_user_id = subject_user_id[0]
    print(f"DEBUG: Retrieved subject_user_id: {subject_user_id}")

    # Fetch selected user's name and role
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT u.role, 
            COALESCE(
                c.class_head, 
                s.subject_head, 
                st.name, 
                CASE 
                    WHEN p.user_id IS NOT NULL THEN CONCAT('Parent of ', st2.name) 
                    ELSE NULL 
                END
            ) AS name
        FROM main_users u
        LEFT JOIN main_classes c ON u.id = c.user_id AND u.role = 'class_head'
        LEFT JOIN main_subjects s ON u.id = s.user_id AND u.role = 'subject_head'
        LEFT JOIN main_students st ON u.id = st.user_id AND u.role = 'student'
        LEFT JOIN main_parents p ON u.id = p.user_id AND u.role = 'parent'
        LEFT JOIN main_students st2 ON p.student_id = st2.roll_no AND u.role = 'parent'
        WHERE u.id = %s
        """, [user_id])

        selected_user = cursor.fetchone()

    if not selected_user:
        print(f"DEBUG: No user found with id {user_id}. Redirecting to chat page.")
        return redirect('subject_head_chat')

    selected_user_role, selected_user_name = selected_user
    print(f"DEBUG: Retrieved selected_user_role: {selected_user_role}, selected_user_name: {selected_user_name}")

    # Handle message sending
    if request.method == "POST":
        message_text = request.POST.get("message", "").strip()
        
        if message_text:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO main_chat (message, sender_id, receiver_id, created_at) 
                    VALUES (%s, %s, %s, %s)
                """, [message_text, subject_user_id, user_id, now()])
            
            print(f"DEBUG: Message sent from {subject_user_id} to {user_id}: {message_text}")
            return redirect('subject_head_chat_user', user_id=user_id)
        else:
            print("DEBUG: Empty message, not sent.")

    # Fetch chat messages between subject head and selected user
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT message, sender_id, receiver_id, created_at 
            FROM main_chat 
            WHERE (sender_id = %s AND receiver_id = %s) 
               OR (sender_id = %s AND receiver_id = %s) 
            ORDER BY created_at ASC
        """, [subject_user_id, user_id, user_id, subject_user_id])

        messages = cursor.fetchall()

    print(f"DEBUG: Retrieved {len(messages)} messages between subject_head_user_id {subject_user_id} and user_id {user_id}")

    return render(request, 'subject_head/subject_head_chat_user.html', {
        'selected_user_role': selected_user_role,
        'selected_user_name': selected_user_name,
        'messages': messages,
        'logged_in_user_id': subject_user_id
    })


######################################################################################################################

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
                    JOIN main_users u ON s.user_id = u.id
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

    print(f"Using student_id: {student_id} for the query.")

    with connection.cursor() as cursor:
        # Fetch the student's name and class ID
        cursor.execute("""
            SELECT s.name, s.class_obj_id
            FROM main_students s 
            WHERE s.id = %s
        """, [student_id])
        student_data = cursor.fetchone()

        if not student_data:
            return redirect('student_login')  # Redirect if student data is invalid

        student_name, class_id = student_data

        class_name = None
        subject_count = 0  # Default to 0 if no subjects are assigned

        if class_id:  # If the student is assigned to a class
            # Fetch the class name
            cursor.execute("""
                SELECT c.class_name 
                FROM main_classes c
                WHERE c.id = %s
            """, [class_id])
            class_data = cursor.fetchone()

            if class_data:
                class_name = class_data[0]

            # Count the number of subjects for this class
            cursor.execute("""
                SELECT COUNT(*) 
                FROM main_subjects 
                WHERE class_obj_id = %s
            """, [class_id])
            subject_count = cursor.fetchone()[0]  # Get the count value

    # Pass data to the template
    return render(request, 'students/student_dashboard.html', {
        'student_name': student_name,
        'class_name': class_name if class_name else "Not Assigned",
        'subject_count': subject_count,
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
            SELECT s.name, s.roll_no, c.class_name, c.class_head, c.email, i.institution_name, s.password
            FROM main_students s
            LEFT JOIN main_classes c ON s.class_obj_id = c.id
            LEFT JOIN main_institution i ON c.institution_id = i.institution_id
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
        # Fetch student details and class head
        cursor.execute("""
            SELECT s.name AS student_name, c.class_name, c.class_head
            FROM main_students s
            LEFT JOIN main_classes c ON s.class_obj_id = c.id
            WHERE s.id = %s
        """, [student_id])
        student_details = cursor.fetchone()

        # Fetch list of students in the same class
        cursor.execute("""
            SELECT s.roll_no, s.name
            FROM main_students s
            WHERE s.class_obj_id = (
                SELECT class_obj_id
                FROM main_students
                WHERE id = %s
            )
        """, [student_id])
        students = cursor.fetchall()

        # Fetch subjects assigned to this class
        cursor.execute("""
            SELECT subject_name, subject_head, email
            FROM main_subjects
            WHERE class_obj_id = (
                SELECT class_obj_id
                FROM main_students
                WHERE id = %s
            )
        """, [student_id])
        subjects = cursor.fetchall()

    # Handle edge cases where student or class data is missing
    if not student_details:
        student_name, class_name, class_head = "Unknown", "Not Assigned", "Not Assigned"
    else:
        student_name, class_name, class_head = student_details

    students_list = [{'roll_no': row[0], 'name': row[1]} for row in students] if students else []
    subjects_list = [{'subject_name': row[0], 'subject_head': row[1], 'email': row[2]} for row in subjects] if subjects else []

    return render(request, 'students/student_class.html', {
        'student_name': student_name,
        'class_name': class_name,
        'class_head': class_head,
        'students': students_list,
        'student_count': len(students_list),
        'subjects': subjects_list,  # Pass subjects to the template
    })


def student_chat(request):
    student_id = request.session.get('student_id')  # Get student ID from session
    if not student_id:
        return redirect('student_login')  # Redirect if not logged in

    # Query to get class_head and subject_heads involved in chat with the logged-in student
    query_recent_chats = '''
        SELECT DISTINCT u.id, u.role
        FROM main_chat c
        JOIN main_users u ON (c.sender_id = u.id OR c.receiver_id = u.id)
        JOIN main_students s ON (s.user_id = c.sender_id OR s.user_id = c.receiver_id)
        WHERE s.id = %s
        AND u.role IN ('class_head', 'subject_head')
    '''
    with connection.cursor() as cursor:
        cursor.execute(query_recent_chats, [student_id])
        users_in_chat = cursor.fetchall()  # Returns [(user_id, role), (user_id, role), ...]

    # Get user IDs from the chat query result
    user_ids_in_chat = [user[0] for user in users_in_chat]

    # Fetch class head names and their user IDs for the users involved in recent chats
    class_heads = list(
        Classes.objects.filter(user_id__in=user_ids_in_chat).values_list('user_id', 'class_head')
    )

    # Fetch subject head names and their user IDs for the users involved in recent chats
    subject_heads = list(
        Subjects.objects.filter(user_id__in=user_ids_in_chat).values_list('user_id', 'subject_head')
    )

    # Query to get suggested users (class head of the student's class + subject heads)
    query_suggested_users = '''
        SELECT u.id, u.role, 
               CASE 
                   WHEN u.role = 'class_head' THEN c.class_head
                   WHEN u.role = 'subject_head' THEN s.subject_head
               END AS name
        FROM main_users u
        LEFT JOIN main_classes c ON u.id = c.user_id
        LEFT JOIN main_subjects s ON u.id = s.user_id
        WHERE u.role IN ('class_head', 'subject_head')
        AND ((c.class_head IS NOT NULL AND c.class_head = (SELECT class_head FROM main_classes WHERE id = (SELECT class_obj_id FROM main_students WHERE id = %s)))
             OR s.subject_head IS NOT NULL)
        AND u.id NOT IN (
            SELECT DISTINCT u.id
            FROM main_chat c
            JOIN main_users u ON (c.sender_id = u.id OR c.receiver_id = u.id)
            JOIN main_students st ON (st.user_id = c.sender_id OR st.user_id = c.receiver_id)
            WHERE st.id = %s
        );
    '''
    with connection.cursor() as cursor:
        cursor.execute(query_suggested_users, [student_id, student_id])
        suggested_users = cursor.fetchall()  # Returns [(user_id, role, name), ...]

    return render(request, 'students/student_chat.html', {
        'class_heads': class_heads,  # Contains [(user_id, class_head_name), ...]
        'subject_heads': subject_heads,  # Contains [(user_id, subject_head_name), ...]
        'suggested_users': suggested_users  # Contains [(user_id, role, name), ...]
    })




def student_chat_user(request, user_id):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('student_login')

    # Fetch the user_id for the logged-in student
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT s.user_id
            FROM main_students s
            WHERE s.id = %s
        """, [student_id])
        student_user_id = cursor.fetchone()

    if not student_user_id:
        messages.error(request, 'Student not found.')
        return redirect('student_dashboard')

    logged_in_user_id = student_user_id[0]

    # Fetch messages between the logged-in student and the selected user
    query = '''
        SELECT message, sender_id, receiver_id, created_at
        FROM main_chat
        WHERE (sender_id = %s AND receiver_id = %s) OR (sender_id = %s AND receiver_id = %s)
        ORDER BY created_at ASC
    '''
    with connection.cursor() as cursor:
        cursor.execute(query, [logged_in_user_id, user_id, user_id, logged_in_user_id])
        messages_fetched = cursor.fetchall()

    # Get the selected user's role
    user = Users.objects.get(id=user_id)
    selected_user_role = user.role

    # Fetch the selected user's name based on their role
    if selected_user_role == 'class_head':
        selected_user_name = Classes.objects.filter(user_id=user_id).values_list('class_head', flat=True).first()
    elif selected_user_role == 'subject_head':
        selected_user_name = Subjects.objects.filter(user_id=user_id).values_list('subject_head', flat=True).first()
    else:
        selected_user_name = 'Unknown'

    # Handle message submission (POST request)
    if request.method == 'POST':
        message_text = request.POST.get('message')
        if message_text:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO main_chat (sender_id, receiver_id, message, created_at)
                    VALUES (%s, %s, %s, NOW())
                """, [logged_in_user_id, user_id, message_text])
            return redirect('student_chat_user', user_id=user_id)

    return render(request, 'students/student_chat_user.html', {
        'messages': messages_fetched,
        'user_id': user_id,
        'logged_in_user_id': logged_in_user_id,  # FIX: Pass logged-in user ID for proper message alignment
        'selected_user_name': selected_user_name,
        'selected_user_role': selected_user_role,
    })





######################################################################################################################

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
                    JOIN main_users u ON p.user_id = u.id
                    WHERE p.student_id = %s AND p.password = %s AND u.role = 'parent'
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
        return redirect('parent_login')  # Redirect to login if not logged in

    with connection.cursor() as cursor:
        # Fetch parent and associated student details
        cursor.execute("""
            SELECT p.id, p.name AS parent_name, p.student_id, 
                   s.name AS student_name, s.class_obj_id
            FROM main_parents p
            JOIN main_students s ON p.student_id = s.roll_no
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

        # Fetch class name and teacher's name
        cursor.execute("""
            SELECT class_name, class_head FROM main_classes
            WHERE id = %s
        """, [student_class_id])
        class_data = cursor.fetchone()
        student_class = class_data[0] if class_data else "Class not assigned"
        class_teacher = class_data[1] if class_data else "No teacher assigned"

        # Fetch subjects count for the class
        cursor.execute("""
            SELECT COUNT(*) FROM main_subjects
            WHERE class_obj_id = %s
        """, [student_class_id])
        subjects_count_data = cursor.fetchone()
        subjects_count = subjects_count_data[0] if subjects_count_data else 0  # Fixed

    # Prepare context for the template
    context = {
        'parent_id': parent_id,
        'parent_name': parent_name,
        'student_id': student_roll_no,
        'student_name': student_name,
        'student_class': student_class,
        'class_teacher': class_teacher,
        'subjects_count': subjects_count
    }

    return render(request, 'parents/parent_dashboard.html', context)


def parent_teacher_profile(request):
    parent_id = request.session.get('parent_id')  # Ensure the parent is logged in
    if not parent_id:
        return redirect('parent_login')

    # Fetch class teacher details
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT c.class_head AS teacher_name, c.email AS teacher_email, 
                   c.class_name, i.institution_name
            FROM main_parents p
            JOIN main_students s ON p.student_id = s.roll_no
            LEFT JOIN main_classes c ON s.class_obj_id = c.id
            LEFT JOIN main_institution i ON c.institution_id = i.institution_id
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


def parent_class(request):
    parent_id = request.session.get('parent_id')  # Ensure the parent is logged in
    if not parent_id:
        return redirect('parent_login')

    with connection.cursor() as cursor:
        # Fetch parent and associated student details
        cursor.execute("""
            SELECT p.id, p.name AS parent_name, p.student_id, 
                   s.name AS student_name, s.class_obj_id 
            FROM main_parents p
            JOIN main_students s ON p.student_id = s.roll_no
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

    # Fetch class details (class name and teacher)
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT class_name, class_head FROM main_classes
            WHERE id = %s
        """, [student_class_id])
        class_data = cursor.fetchone()
    student_class = class_data[0] if class_data else "Class not assigned"
    class_teacher = class_data[1] if class_data else "No teacher assigned"

    # Fetch subjects for the class
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT subject_name, subject_head, email FROM main_subjects
            WHERE class_obj_id = %s
        """, [student_class_id])
        subjects = cursor.fetchall()

    # Fetch students of the class
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT roll_no, name FROM main_students
            WHERE class_obj_id = %s
        """, [student_class_id])
        students = cursor.fetchall()

    # Prepare context for the template
    context = {
        'parent_name': parent_name,
        'student_name': student_name,
        'student_class': student_class,
        'class_teacher': class_teacher,
        'subjects': subjects,
        'students': students,
        'student_count': len(students)  # Total number of students in the class
    }

    return render(request, 'parents/parent_class.html', context)



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
                   c.class_name, 
                   c.class_head AS teacher_name, c.email AS teacher_email
            FROM main_parents p
            JOIN main_students s ON p.student_id = s.roll_no
            LEFT JOIN main_classes c ON s.class_obj_id = c.id
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



def parent_chat(request):
    parent_id = request.session.get('parent_id')  # Get parent ID from session
    if not parent_id:
        return redirect('parent_login')  # Redirect to login if not logged in

    print(f"Parent ID for chat: {parent_id}")

    with connection.cursor() as cursor:
        # Get the parent's user ID
        cursor.execute("SELECT user_id FROM main_parents WHERE id = %s", [parent_id])
        user_id = cursor.fetchone()

        if not user_id:
            print("No user_id found for this parent.")
            return render(request, 'parents/parent_chat.html', {'chat_users': [], 'suggested_users': []})

        user_id = user_id[0]
        print(f"User ID for parent: {user_id}")

        # Get recent chat users (Users the parent has already chatted with)
        cursor.execute("""
            SELECT DISTINCT u.id, 
                            COALESCE(c.class_head, s.subject_head) AS name, 
                            u.role
            FROM main_chat ch
            JOIN main_users u ON (ch.sender_id = u.id OR ch.receiver_id = u.id)
            LEFT JOIN main_classes c ON u.id = c.user_id
            LEFT JOIN main_subjects s ON u.id = s.user_id
            WHERE (ch.sender_id = %s OR ch.receiver_id = %s)
            AND u.role IN ('class_head', 'subject_head')
        """, [user_id, user_id])

        chat_users = cursor.fetchall()
        print(f"Recent chat users: {chat_users}")

        recent_chat_user_ids = {user[0] for user in chat_users}  # Extract only user IDs for easy checking
        print(f"Recent chat user IDs: {recent_chat_user_ids}")

        # Get the class_head of the student's class
        cursor.execute("""
            SELECT c.user_id, c.class_head
            FROM main_classes c
            JOIN main_students st ON st.class_obj_id = c.id
            WHERE st.id = (SELECT student_id FROM main_parents WHERE id = %s)
        """, [parent_id])
        class_head = cursor.fetchone()

        class_head_id = class_head[0] if class_head else None
        print(f"Class Head: {class_head}")

        # Get suggested users excluding those in recent chats
        cursor.execute("""
            SELECT u.id, u.role, 
                CASE 
                    WHEN u.role = 'class_head' THEN c.class_head
                    WHEN u.role = 'subject_head' THEN s.subject_head
                END AS name
            FROM main_users u
            LEFT JOIN main_classes c ON u.id = c.user_id
            LEFT JOIN main_subjects s ON u.id = s.user_id
            WHERE u.role IN ('class_head', 'subject_head')
            AND (
                (c.class_head IS NOT NULL AND c.class_head = (SELECT class_head FROM main_classes WHERE id = (SELECT class_obj_id FROM main_students WHERE roll_no = (SELECT student_id FROM main_parents WHERE id = %s))))
                OR s.subject_head IS NOT NULL
            )
            AND u.id NOT IN (
                SELECT DISTINCT u.id
                FROM main_chat ch
                JOIN main_users u ON (ch.sender_id = u.id OR ch.receiver_id = u.id)
                WHERE (ch.sender_id = %s OR ch.receiver_id = %s)
            )
        """, [parent_id, user_id, user_id])

        suggested_users = cursor.fetchall()
        print(f"Suggested users before adding class head: {suggested_users}")

        suggested_user_ids = {user[0] for user in suggested_users}  # Extract user IDs for easy checking

        # Ensure the class head is suggested if they haven't been messaged yet
        if class_head_id and class_head_id not in recent_chat_user_ids and class_head_id not in suggested_user_ids:
            print(f"Adding class head to suggested users: {class_head}")
            suggested_users.append((class_head_id, 'class_head', class_head[1]))

        print(f"Final suggested users: {suggested_users}")

    return render(request, 'parents/parent_chat.html', {
        'chat_users': chat_users,
        'suggested_users': suggested_users,
    })


def parent_chat_user(request, user_id):
    parent_id = request.session.get('parent_id')
    if not parent_id:
        return redirect('parent_login')

    # Fetch the parent’s user_id
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT p.user_id
            FROM main_parents p
            WHERE p.id = %s
        """, [parent_id])
        parent_user_id = cursor.fetchone()

    if not parent_user_id:
        messages.error(request, 'Parent not found.')
        return redirect('parent_dashboard')

    # Debugging: Print the parent's user_id
    print(f"Parent's user_id for chat: {parent_user_id[0]}")

    # Fetch messages between the logged-in parent and the selected user
    query = '''
        SELECT message, sender_id, receiver_id, created_at
        FROM main_chat
        WHERE (sender_id = %s AND receiver_id = %s) OR (sender_id = %s AND receiver_id = %s)
        ORDER BY created_at ASC
    '''
    with connection.cursor() as cursor:
        cursor.execute(query, [parent_user_id[0], user_id, user_id, parent_user_id[0]])
        messages_fetched = cursor.fetchall()

    # Debugging: Print the fetched messages
    print(f"Messages fetched: {messages_fetched}")

    # Get the selected user's role
    user = Users.objects.get(id=user_id)
    selected_user_role = user.role

    # Fetch the selected user's name based on their role
    if selected_user_role == 'class_head':
        selected_user_name = Classes.objects.filter(user_id=user_id).values_list('class_head', flat=True).first()
    elif selected_user_role == 'subject_head':
        selected_user_name = Subjects.objects.filter(user_id=user_id).values_list('subject_head', flat=True).first()
    else:
        selected_user_name = 'Unknown'

    # Fetch the teacher's user_id for message sender identification
    if selected_user_role == 'class_head':
        teacher_user_id = Classes.objects.filter(class_head=user_id).values_list('user_id', flat=True).first()
    else:
        teacher_user_id = Subjects.objects.filter(subject_head=user_id).values_list('user_id', flat=True).first()

    # Handle message submission (POST request)
    if request.method == 'POST':
        message_text = request.POST.get('message')
        if message_text:
            # Save the new message to the database
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO main_chat (sender_id, receiver_id, message, created_at)
                    VALUES (%s, %s, %s, NOW())
                """, [parent_user_id[0], user_id, message_text])

            # Redirect the user back to the chat page to see the new message
            return redirect('parent_chat_user', user_id=user_id)

    return render(request, 'parents/parent_chat_user.html', {
        'messages': messages_fetched, 
        'user_id': user_id,
        'logged_in_user_id': parent_user_id[0],  # Pass this for sender alignment
        'selected_user_name': selected_user_name,
        'selected_user_role': selected_user_role,
        'teacher_user_id': teacher_user_id
    })



######################################################################################################################


