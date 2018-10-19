from django import forms
from .models import Profile,Post,User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude = ['user']
        fields = ['username','profile_image','neighbourhood','location']

class PostForm(forms.ModelForm):
    image_name = forms.CharField(max_length = 30)

    class Meta:
        model = Post
        fields = ['post','image','link','post_description']

class BusinessForm(forms.ModelForm):
    name = forms.CharField(max_length = 30)

    class Meta:
        model = Post
        fields = ['name','product','description']


