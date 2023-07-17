from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Ваш нікнейм", widget=forms.TextInput(attrs={'placeholder': "Ваш нікнейм"}))
    password1 = forms.CharField(label="Пароль:", widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(label="Повтор пароля:",
                                widget=forms.PasswordInput(attrs={'placeholder': 'Повтор пароля'}))
    email = forms.CharField(label="Email:", widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")


class AuthenticationUserForm(AuthenticationForm):
    username = forms.CharField(label="Ваш нікнейм", widget=forms.TextInput(attrs={'placeholder': "Ваш нікнейм"}))
    password = forms.CharField(label="Пароль:", widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
