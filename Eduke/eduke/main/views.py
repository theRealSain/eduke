from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import InstitutionRegisterForm
from .models import Institution
from .forms import LoginForm
from django.contrib.auth import logout

def index(request):
    return render(request, 'index.html')

# @login_required
def admin_dashboard(request):
    # Retrieve session data
    institution_name = request.session.get('institution_name', 'Admin')

    return render(request, 'admin/admin_dashboard.html', {'institution_name': institution_name})


def register_institution(request):
    if request.method == 'POST':
        print("Received POST request")  # Debugging
        form = InstitutionRegisterForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Debugging
            institution_name = form.cleaned_data['institution_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']  # Unhashed password

            if Institution.objects.filter(email=email).exists():
                print("Email already exists")  # Debugging
                form.add_error('email', 'An institution with this email already exists.')
            else:
                try:
                    # Create the institution with the plain password (no hashing)
                    Institution.objects.create(
                        institution_name=institution_name,
                        email=email,
                        password=password  # Store plain password here
                    )
                    print("Institution created successfully")  # Debugging

                    # Redirect to login page with a success message
                    messages.success(request, 'Institution registered successfully! Please log in.')
                    return redirect('login')  # Redirect to the login page
                except Exception as e:
                    print(f"Error while creating institution: {e}")  # Debugging
                    form.add_error(None, 'An error occurred while saving the data. Please try again.')
        else:
            print("Form is invalid")  # Debugging
            print(form.errors)  # Debugging: Log form errors
    else:
        print("GET request received")  # Debugging
        form = InstitutionRegisterForm()

    return render(request, 'registration/institution_register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Check if the email and password match an institution in the database
            try:
                institution = Institution.objects.get(email=email, password=password)
                # If matched, start a session
                request.session['institution_id'] = institution.id
                request.session['institution_name'] = institution.institution_name

                # Redirect to the admin dashboard
                return redirect('admin_dashboard')

            except Institution.DoesNotExist:
                # If no match, show an error
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def admin_logout(request):
    logout(request)  # Logs out the user and destroys the session
    return redirect('login')  # Redirect to the admin login page