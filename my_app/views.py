from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def welcome(request):
    return render(request, 'my_app/home.html')
@login_required
def student_home(request):
    return render(request, 'my_app/student_home.html')

@login_required
def instructor_home(request):
    return render(request, 'my_app/instructor_home.html')

@login_required
def admin_home(request):
    return render(request, 'my_app/admin_home.html')


