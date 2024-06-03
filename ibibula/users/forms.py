from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField()
    password = forms.CharField()

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "phone_number",
            "telegram",
        )
    
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    phone_number = forms.CharField()
    telegram = forms.CharField()


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "phone_number",
            "telegram",
            "password1",
            "password2"
            "image",
        )
    username = forms.CharField()
    email = forms.CharField()
    phone_number = forms.CharField()
    telegram = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    image = forms.ImageField(required=False)