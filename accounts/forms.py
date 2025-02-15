# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    role = forms.ChoiceField(choices=[('patient', 'Patient'), ('doctor', 'Doctor')])

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']