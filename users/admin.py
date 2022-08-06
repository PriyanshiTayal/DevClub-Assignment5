from django.contrib import admin
from .models import Instructor, Student, Course, Admin, Session, Subject, CustomUser

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','username')

class InstructorAdmin(admin.ModelAdmin):
    list_display = ('id','gender','profile_pic')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','gender','profile_pic','session_year_id')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','course_name')

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id','subject_name','course_id','instructor_id')

class AdminAdmin(admin.ModelAdmin):
    list_display = ('id','profile_pic')

class SessionAdmin(admin.ModelAdmin):
    list_display = ('id','start_year','end_year')

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Admin, AdminAdmin)
admin.site.register(Session, SessionAdmin)