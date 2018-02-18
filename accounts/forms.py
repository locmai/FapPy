from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import UserManagement


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=255, required=True, widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm your password',
        }


class SupervisorForms(forms.ModelForm):
    class Meta:
        model = UserManagement
        fields = ('supervisor',)
        labels = {
            'supervisor': 'Select your supervisor',
        }