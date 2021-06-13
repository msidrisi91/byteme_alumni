from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=32, help_text='First name')
    last_name = forms.CharField(max_length=32, help_text='Last name')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=32, help_text='First name')
    last_name = forms.CharField(max_length=32, help_text='Last name')
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gender','mobile_number','college','roll_number','course','passing_year','image']