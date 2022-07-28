from django.shortcuts import redirect, render

from django.contrib import messages
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

def profile(request):
    return render(request, 'my_learning_app/profile.html')
