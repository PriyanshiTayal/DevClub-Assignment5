from urllib import request
from django.shortcuts import redirect, render

from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Course, CustomUser,Admin,Instructor,Student,Session
from .forms import UserRegisterForm, UserUpdateForm, StudentUpdateForm, InstructorUpdateForm, AdminUpdateForm, AddStaffForm

# GENERAL VIEWS
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            
            user = CustomUser.objects.create_user(username = username,email = email,
                                                    password = password,
                                                    first_name = first_name,
                                                    last_name = last_name)
            user.save()                             
            Admin.objects.create(admin=user)
            messages.success(request, f'{username}, Your Account has been Created Successfully. Now LogIn to Start Learning!')
            return redirect('login')           
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html', {'form': form})

def login(request):
    return render(request, 'users/login.html')
 
def dologin(request):
     
    print("here")
    username = request.GET.get('username')
    password = request.GET.get('password')
    # user_type = request.GET.get('user_type')
    print(username)
    print(password)
    print(request.user)
    if not (username and password):
        messages.error(request, "Please provide all the details!!")
        return render(request, 'users/login.html')
 
    user = authenticate(username=username, password=password)
    if user is None:
        messages.error(request, 'Invalid Login Credentials!!')
        return render(request, 'users/login.html')
 
    auth_login(request, user)
    print(request.user)
 
    if user.user_type == '3':
        return redirect('student_home')
    elif user.user_type == '2':
        return redirect('instructor_home')
    elif user.user_type == '1':
        return redirect('admin_home')
 
    return render(request, 'my_app/home.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if request.user.user_type == '1':
            p_form = AdminUpdateForm(request.POST,request.FILES,instance=request.user.admin)
        elif request.user.user_type == '2':
            p_form = InstructorUpdateForm(request.POST,request.FILES,instance=request.user.instructor)
        elif request.user.user_type == '3':
            p_form = StudentUpdateForm(request.POST,request.FILES,instance=request.user.student)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f' Your Account has been Updated Successfully!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        if request.user.user_type == '1':
            p_form = AdminUpdateForm(instance=request.user.admin)
        elif request.user.user_type == '2':
            p_form = InstructorUpdateForm(instance=request.user.instructor)
        elif request.user.user_type == '3':
            p_form = StudentUpdateForm(instance=request.user.student)
    context={
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request, 'users/profile.html', context)


#ADMIN VIEWS
def admin_check(user):
    return user.is_authenticated and user.user_type == '1' 

@login_required()
@user_passes_test(admin_check)
def add_staff(request):
    if request.method == 'POST':
        form = AddStaffForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            gender= form.cleaned_data['gender']
            address=form.cleaned_data['address']
            
            user = CustomUser.objects.create_user(username = username,email = email,
                                                    password = password,
                                                    first_name = first_name,
                                                    last_name = last_name, user_type = 2)
            user.instructor.gender = gender
            user.instructor.address = address
            user.save()      
                      
            messages.success(request, f'{username} has been Added as an Instructor Successfully!')
            return redirect('add_staff')           
    else:
        form = AddStaffForm()
    return render(request,'users/add_staff.html', {'form': form})
    
@user_passes_test(admin_check)
def add_course(request):
    if request.method == 'POST':
        course = request.POST.get('course')

        course = Course(course_name = course)
        course.save()
        messages.success(request, f'Course {course} Added Successfully!')
        return redirect('add_course')
    else:
        return render(request,'users/add_course.html')

