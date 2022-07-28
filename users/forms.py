from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()


    class Meta:
        model = CustomUser
        fields = ['username','email','first_name','last_name','password1','password2']
