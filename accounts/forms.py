from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'industry',
            'experience',
            'profile_picture'
        ]   