from django import forms
from .models import CustomUser, Student, Admin, Instructor
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()


    class Meta:
        model = CustomUser
        fields = ['username','email','first_name','last_name','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = CustomUser
        fields = ['username','email','first_name','last_name']

class StudentUpdateForm(forms.ModelForm):  
    class Meta:
        model = Student
        fields = ['gender','address','profile_pic']

class InstructorUpdateForm(forms.ModelForm):  
    class Meta:
        model = Instructor
        fields = ['gender','address','profile_pic']

class AdminUpdateForm(forms.ModelForm):  
    class Meta:
        model = Admin
        fields = ['profile_pic']