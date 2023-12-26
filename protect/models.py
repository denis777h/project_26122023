from django.contrib.auth import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import *


# Create your models here.

class BaseRegisterForm(UserCreationForm):
    login = forms.CharField(label="Логин:")
    password = forms.CharField(label="Пароль:")
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ("Username",
                  "first_name",
                  "last_name",
                  "Email",
                  "password",)
