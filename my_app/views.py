from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, 'my_app/home.html')

def student_home(request):
    return render(request, 'my_app/student_home.html')
def instructor_home(request):
    return render(request, 'my_app/instructor_home.html')
def admin_home(request):
    return render(request, 'my_app/admin_home.html')


