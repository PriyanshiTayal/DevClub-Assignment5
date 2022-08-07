from urllib import request
from django.forms import ChoiceField
from django.shortcuts import redirect, render

from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Course, CustomUser,Admin,Instructor,Student,Session, Subject
from .forms import  DocumentForm, UserRegisterForm, UserUpdateForm, StudentUpdateForm, InstructorUpdateForm, AdminUpdateForm, AddStaffForm
from documents.models import Document

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
            user_type = form.cleaned_data['user_type']
            user = CustomUser.objects.create_user(username = username,email = email,
                                                    password = password,
                                                    first_name = first_name,
                                                    last_name = last_name, user_type = user_type)
                            
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


@login_required()
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

@login_required
def add_subject(request):
    courses = Course.objects.all()
    instructors = Instructor.objects.all()
    context = {
        'instructors': instructors,
        'courses' : courses
    } 
    return render(request,'users/add_subject.html',context)
@login_required
def add_subject_save(request):
    if request.method == 'POST':
            subject_name = request.POST.get['subject']
            course_id = request.POST.get['course']
            instructor_id = request.POST.get['instructor']
            course = Course.objects.get(id = course_id)
            instructor = Instructor.objects.get(id == instructor_id)
            sub = Subject(subject_name = subject_name, course_id = course, instructor_id = instructor)
            sub.save()
            messages.success(request, f'Subject Added Successfully!')
            return redirect('add_subject')
    else:
        return render(request,'users/add_subject.html')

@login_required
def add_course(request):
    if request.method == "POST":
        course = request.POST.get('course')
        course_model = Course(course_name=course)
        course_model.save()
        messages.success(request, "Course Added Successfully!")            
        return redirect('add_course')
    else:
        return render(request, "users/add_course.html")

@login_required
def add_session(request):
    if request.method == "POST":
        start_year = request.POST.get('start_year')
        end_year = request.POST.get('end_year')

        sessionyear = Session(start_year=start_year,end_year=end_year)
        sessionyear.save()
        messages.success(request, "Session Year added Successfully!")
        return redirect("add_session")
    else:
        return render(request, "users/add_session.html")

#Instructor Views
@login_required
def instructor_subjects(request):
    context = {
        'subjects': request.user.instructor.subject_set.all()
    }
    return render(request, "users/instructor_subjects.html", context)

#Student Views
@login_required
def student_subjects(request):
    context = {
        'subjects': request.user.student.course_id.subject_set.all()
    }    
    return render(request, "users/student_subjects.html", context)

@login_required
def subject_detail(request,sub):
    subject = Subject.objects.get(subject_name = sub)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            doc = form.cleaned_data['doc']
            description = form.cleaned_data['description']
            Doc = Document.objects.create(title = title,doc = doc, description = description, subject_id = subject)
            Doc.save()
            messages.success(request, "Document Uploaded Successfully!") 
            return redirect('my_subjects')
    else:
        form = DocumentForm()
        uploaded_docs = Document.objects.filter(subject_id = subject)
    return render(request, "users/subject_detail.html", {'form':form, 'subject':subject, 'docs':uploaded_docs})