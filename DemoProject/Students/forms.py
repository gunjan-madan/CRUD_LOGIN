from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields='__all__'


class SignupForm(UserCreationForm):
    class Meta:
        model= User
        fields=['username','first_name', 'last_name', 'email']