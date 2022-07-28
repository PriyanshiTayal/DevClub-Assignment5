from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, 'my_app/home.html')

def profile(request):
    return render(request, 'my_app/profile.html')