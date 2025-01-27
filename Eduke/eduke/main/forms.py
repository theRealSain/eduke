from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Institution, Classes

class InstitutionRegisterForm(forms.ModelForm):
    class Meta:
        model = Institution  # Link to your Institution model
        fields = ['institution_name', 'email', 'password']  # Specify fields to include

        # Add widgets to customize the form appearance
        widgets = {
            'institution_name': forms.TextInput(attrs={
                'class': 'border border-gray-400 rounded-lg p-2 w-full mb-4 focus:outline-none focus:ring-2 focus:ring-[#4f0074]',
                'placeholder': 'Institution Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'border border-gray-400 rounded-lg p-2 w-full mb-4 focus:outline-none focus:ring-2 focus:ring-[#4f0074]',
                'placeholder': 'Email Address'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'border border-gray-400 rounded-lg p-2 w-full mb-4 focus:outline-none focus:ring-2 focus:ring-[#4f0074]',
                'placeholder': 'Password'
            }),
        }

    def save(self, commit=True):
        """Override save to hash the password before saving."""
        institution = super().save(commit=False)
        if commit:
            institution.save()
        return institution
    
# Form for user login (authentication)
class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'border border-gray-400 rounded-lg p-2 w-full mb-4 focus:outline-none focus:ring-2 focus:ring-[#4f0074]',
            'placeholder': 'Email Address'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'border border-gray-400 rounded-lg p-2 w-full mb-4 focus:outline-none focus:ring-2 focus:ring-[#4f0074]',
            'placeholder': 'Password'
        })
    )

class AddClassForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = ['name']  # Only need the class name for now

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'px-4 py-2 border rounded-md',
            'placeholder': 'Enter class name',
            'required': True
        })


class TeacherLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'block w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none',
            'placeholder': 'Enter your email',
            'id': 'email',
        }),
        label='Email Address'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none',
            'placeholder': 'Enter your password',
            'id': 'password',
        }),
        label='Password'
    )

class StudentLoginForm(forms.Form):
    roll_no = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none',
            'placeholder': 'Enter your Roll No.',
            'id': 'roll_no',
        }),
        label="Roll No."
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none',
            'placeholder': 'Enter your Password',
            'id': 'password',
        }),
        label="Password"
    )

class ParentLoginForm(forms.Form):
    roll_no = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none',
            'placeholder': 'Enter your Roll No.',
            'id': 'roll_no',
        }),
        label="Roll No."
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'block w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none',
        'placeholder': 'Enter your password',
        'id': 'password'
    }))