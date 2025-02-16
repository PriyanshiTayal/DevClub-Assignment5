from unittest.util import _MAX_LENGTH
from django import forms
from .models import Course, CustomUser, Student, Admin, Instructor, Subject
from django.contrib.auth.forms import UserCreationForm
from documents.models import Document

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = CustomUser
        fields = ['username','email','first_name','last_name','user_type','password1','password2']

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

class AddStaffForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    gender_data = (("MALE","MALE"),("FEMALE","FEMALE"),("OTHER","OTHER"))
    gender = forms.ChoiceField(choices=gender_data)
    address = forms.CharField(max_length=100)
    class Meta:
        model = CustomUser
        fields = ['username','email','first_name','last_name','gender','password1','password2','address']

class AddStudentForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    gender_data = (("MALE","MALE"),("FEMALE","FEMALE"),("OTHER","OTHER"))
    gender = forms.ChoiceField(choices=gender_data)
    address = forms.CharField(max_length=100)
    class Meta:
        model = CustomUser
        fields = ['username','email','first_name','last_name','gender','password1','password2','address']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title','doc','description']