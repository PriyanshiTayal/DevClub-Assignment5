from django.shortcuts import redirect, render

from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import CustomUser,Admin,Instructor,Student
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            
            user = CustomUser()
            user.username = username
            user.email = email
            user.password = password
            user.first_name = first_name
            user.last_name = last_name
            user.save()                             
            Admin.objects.create(admin=user)
            messages.success(request, f'{username}, Your Account has been created successfully. Now LogIn to start Learning!')
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
 
    user = CustomUser.objects.filter(username=username, password=password).last()
    if not user:
        messages.error(request, 'Invalid Login Credentials!!')
        return render(request, 'users/login.html')
 
    auth_login(request, user)
    print(request.user)
 
    if user.user_type == CustomUser.STUDENT:
        return redirect('student_home')
    elif user.user_type == CustomUser.INSTRUCTOR:
        return redirect('instructor_home')
    elif user.user_type == CustomUser.ADMIN:
        return redirect('admin_home')
 
    return render(request, 'my_app/home.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')
