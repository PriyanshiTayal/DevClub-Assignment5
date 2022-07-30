from django.db import models
from tkinter import CASCADE
from django.contrib.auth.models import AbstractUser
from PIL import Image
# Create your models here.

class CustomUser(AbstractUser):
    ADMIN = '1'
    INSTRUCTOR = '2'
    STUDENT = '3'
 
    user_type_data = ((ADMIN, "ADMIN"), (INSTRUCTOR, "Instructor"), (STUDENT, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)

class Session(models.Model):
    start_year = models.DateField()
    end_year = models.DateField()

class Admin(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    profile_pic = models.ImageField(default ='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.admin.username}'
    def save(self):
        super().save()
        img = Image.open(self.profile_pic.path)
        if img.height> 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

class Instructor(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    profile_pic = models.ImageField(default ='default.jpg', upload_to='profile_pics')
    gender_data = (("MALE","MALE"),("FEMALE","FEMALE"),("OTHER","OTHER"))
    gender = models.CharField(default='MALE',choices=gender_data,max_length=20)
    address = models.TextField()

    def __str__(self):
        return f'{self.admin.username}'
    def save(self):
        super().save()
        img = Image.open(self.profile_pic.path)
        if img.height> 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

class Course(models.Model):
    course_name = models.CharField(max_length=10)
    instructor_id = models.ForeignKey(Instructor, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.course_name}'


class Student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    profile_pic = models.ImageField(default ='default.jpg', upload_to='profile_pics')
    gender_data = (("MALE","MALE"),("FEMALE","FEMALE"),("OTHER","OTHER"))
    gender = models.CharField(default='MALE',choices=gender_data,max_length=20)
    address = models.TextField()
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING, default=1)
    session_year_id = models.ForeignKey(Session, null=True, blank = True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.admin.username}'

    def save(self):
        super().save()
        img = Image.open(self.profile_pic.path)
        if img.height> 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)