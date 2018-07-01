from django import forms
from django.contrib.auth.models import User
from app_login import UserProfileInfo

class userForm(forms.ModelForm):
    password = forms.Charfield(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')