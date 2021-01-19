from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from webApp.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['fName', 'lName', 'email', 'password']