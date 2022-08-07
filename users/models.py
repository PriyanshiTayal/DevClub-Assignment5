from django.db import models
from urllib import request
from tkinter import CASCADE
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import messages
# Create your models here.

class CustomUser(AbstractUser):
    ADMIN = '1'
    INSTRUCTOR = '2'
    STUDENT = '3'
 
    user_type_data = ((ADMIN, "ADMIN"), (INSTRUCTOR, "Instructor"), (STUDENT, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)

class Session(models.Model):
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    objects = models.Manager()

class Admin(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    profile_pic = models.ImageField(default ='default.jpg', upload_to='profile_pics')
    objects = models.Manager() 

    def __str__(self):
        return f'{self.admin.username}'
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
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
    address = models.TextField(default = "")
    objects = models.Manager()

    def __str__(self):
        return f'{self.admin.username}'
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profile_pic.path)
        if img.height> 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    objects = models.Manager()
    def __str__(self):
        return f'{self.course_name}'

class Subject(models.Model):
    subject_name = models.CharField(max_length=10,unique=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, default=Course.objects.first().pk)
    instructor_id = models.ForeignKey(Instructor, on_delete=models.DO_NOTHING)
    objects = models.Manager()

    def __str__(self):
        return f'{self.subject_name}'


class Student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    profile_pic = models.ImageField(default ='default.jpg', upload_to='profile_pics')
    gender_data = (("MALE","MALE"),("FEMALE","FEMALE"),("OTHER","OTHER"))
    gender = models.CharField(default='MALE',choices=gender_data,max_length=20)
    address = models.TextField(default="")
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING,default = Course.objects.first().pk)
    session_year_id = models.ForeignKey(Session, null=True, blank = True, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return f'{self.admin.username}'

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profile_pic.path)
        if img.height> 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == '1':
            Admin.objects.create(admin=instance)
        elif instance.user_type == '2':
            Instructor.objects.create(admin=instance)
        elif instance.user_type == '3':
            Student.objects.create(admin=instance)
        else:
            print('error1')

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == '1':
        instance.admin.save()
    elif instance.user_type == '2':
        instance.instructor.save()
    elif instance.user_type == '3':
        instance.student.save()
    else:
        print('error2')