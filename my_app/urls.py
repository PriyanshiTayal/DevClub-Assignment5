from django.urls import path
from . import views

urlpatterns = [
    path('student/',views.welcome, name='student_home'),
    path('instructor/',views.welcome, name='instructor_home'),
    path('admin/',views.welcome, name='admin_home'),
]