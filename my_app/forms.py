from django import forms
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from . import models

class SignUpForm(forms.Form):
    user_name = forms.CharField(max_length=100, required=True, label='User Name')
    first_name = forms.CharField(max_length=100)  
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User

    # def __str__(self) -> str:
    #     return f'{self.first_name} {self.last_name}'


class CreatePostForm(ModelForm):
    class Meta:
        model = models.CreatePost
        fields = ['picture', 'caption', 'body']