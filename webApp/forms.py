from django import forms
from webApp.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['fName', 'lName', 'email', 'password']