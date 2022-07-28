from django.contrib import admin
from .models import Instructor, Student, Course, Admin

# Register your models here.
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('gender','profile_pic')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('gender','profile_pic','session_year_id')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name','instructor_id')




admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Admin)
