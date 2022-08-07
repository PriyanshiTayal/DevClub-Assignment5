from statistics import mode
from django.db import models
from users.models import Instructor, Student

# Create your models here.
class InstructorFeedback(models.Model):
    instructor_id = models.ForeignKey(Instructor, on_delete= models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField(default = "")
    sent_at = models.DateTimeField(auto_now_add=True)

class StudentFeedback(models.Model):
    student_id = models.ForeignKey(Student, on_delete= models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField(default = "")
    sent_at = models.DateTimeField(auto_now_add=True)