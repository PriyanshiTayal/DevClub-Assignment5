from unittest.util import _MAX_LENGTH
from django import forms
from .models import Course, CustomUser, Student, Admin, Instructor, Subject
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

class AddStaffForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    gender_data = (("MALE","MALE"),("FEMALE","FEMALE"),("OTHER","OTHER"))
    gender = forms.ChoiceField(choices=gender_data)
    address = forms.CharField(max_length=100)

    fields = ['username','email','first_name','last_name','gender','password1','password2','address']

class AddSubjectForm(forms.ModelForm):
    instructor_all = Instructor.objects.all()
    instructor_name_list = []
    for instructor in instructor_all:
        instructor_name_list.append(instructor.admin.username)
    instructor_id = forms.ChoiceField(choices=instructor_name_list)
    class Meta:
        model = Subject
        fields = ['subject_name','instructor_id']