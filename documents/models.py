from sys import maxsize
from time import timezone
from tkinter import CASCADE
from django.db import models
from users.models import Subject


# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=255, default = "Document")
    doc = models.FileField(upload_to = 'Docs')
    subject_id = models.ForeignKey(Subject, on_delete= models.CASCADE)
    description = models.TextField(default = "")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.subject_id.subject_name, self.title}'