from django.urls import path
from . import views

urlpatterns = [
    path('student/',views.student_home, name='student_home'),
    path('instructor/',views.instructor_home, name='instructor_home'),
    path('admin/',views.admin_home, name='admin_home'),
]