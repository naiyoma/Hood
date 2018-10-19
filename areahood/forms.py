from django import forms
from .models import Profile,Post,User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude = ['user']
        fields = ['username','profile_image']
