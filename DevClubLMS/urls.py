"""DevClubLMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from my_app import views as myapp_views
from communication import views as comm_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myapp_views.welcome, name='app-home'),
    path('home/', include('my_app.urls')),
    path('login/',user_views.login , name = 'login'),
    path('dologin/',user_views.dologin , name = 'dologin'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name = 'logout'),
    path('register/', user_views.register, name = 'register'),
    path('profile/', user_views.profile, name = 'profile'),

    #ADMIN URLS
    path('add_instructor/', user_views.add_staff, name = 'add_staff'),
    path('add_subject/', user_views.add_subject, name = 'add_subject'),
    path('add_course/', user_views.add_course, name = 'add_course'),
    path('add_session/', user_views.add_session, name = 'add_session'),
    path('add_subject_save/', user_views.add_subject_save, name = 'add_subject_save'),
    path('instructor_feed_reply/', comm_views.instructor_feed_reply, name = 'instructor_feed_reply'),
    path('student_feed_reply/', comm_views.student_feed_reply, name = 'student_feed_reply'),

    #INSTRUCTOR URLS
    path('instructor_subjects/', user_views.instructor_subjects, name = 'instructor_subjects'), 
    path('instructor_feedback/', comm_views.instructor_feedback, name = 'instructor_feedback'), 
    

    #STUDENT URLS
    path('student_subjects/', user_views.student_subjects, name = 'student_subjects'),
    path('subject/<slug:sub>', user_views.subject_detail, name = 'subject_detail'), 
    path('student_feedback/', comm_views.student_feedback, name = 'student_feedback'),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)