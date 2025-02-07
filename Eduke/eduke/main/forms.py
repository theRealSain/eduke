from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Institution, Classes, Users, Subjects

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


class ClassHeadLoginForm(forms.Form):
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

class SubjectHeadLoginForm(forms.Form):
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


#######################################################################################################################


class AddClassForm(forms.ModelForm):
    class_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-1/5 px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none',
            'placeholder': 'Enter Class Name',
            'id': 'class_name',
        })
    )
    class_head = forms.CharField(  # Keeping class_head as a text field
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-1/5 px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none',
            'placeholder': 'Enter Class Head Name',
            'id': 'class_head',
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-1/5 px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none',
            'placeholder': 'Enter Email',
            'id': 'email',
        })
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={
            'class': 'w-1/5 px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none',
            'placeholder': 'Enter Password',
            'id': 'password',
            'onfocus': 'this.type="text"',
            'onblur': 'this.type="password"'
        })
    )

    class Meta:
        model = Classes
        fields = ['class_name', 'class_head', 'email', 'password']


class AddSubjectForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ['subject_name', 'subject_head', 'email', 'password']

    subject_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-1/5 px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none',
            'placeholder': 'Enter Subject Name',
            'id': 'subject_head',
        })
    )
    subject_head = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-1/5 px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none',
            'placeholder': 'Enter Subject Head Name',
            'id': 'subject_head',
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-1/5 px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none',
            'placeholder': 'Enter Email',
            'id': 'email',
        })
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={
            'class': 'w-1/5 px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none',
            'placeholder': 'Enter Password',
            'id': 'password',
            'onfocus': 'this.type="text"',
            'onblur': 'this.type="password"'
        })
    )



