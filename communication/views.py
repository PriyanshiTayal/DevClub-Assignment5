from django.shortcuts import render, redirect
from users.models import Instructor, Student
from .models import InstructorFeedback, StudentFeedback
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def instructor_feedback(request):
    instructor = Instructor.objects.get(admin=request.user.id)
    feedback_data = InstructorFeedback.objects.filter(instructor_id=instructor)
    if request.method == "POST":
        feedback = request.POST.get('feedback')

        add_feedback = InstructorFeedback(feedback=feedback,instructor_id=instructor)
        add_feedback.save()
        messages.success(request, "Feedback Sent Successfully!")
        return redirect('instructor_feedback')
    else:
        context = {
            "feedback_data":feedback_data
        }
        return render (request, "communication/instructor_feedback.html", context)


@login_required
def instructor_feed_reply(request):
    if request.method == "POST":
        feedback_id = request.POST.get('id')
        feedback_reply = request.POST.get('reply')
        feedback = InstructorFeedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.save()
        messages.success(request, "Reply Sent Successfully!")
        return redirect('instructor_feed_reply')

    else:
        feedbacks = InstructorFeedback.objects.all()
        context = {
            "feedbacks": feedbacks
        }
    return render(request, 'communication/instructor_feed_reply.html', context)

@login_required
def student_feedback(request):
    student = Student.objects.get(admin=request.user.id)
    feedback_data = StudentFeedback.objects.filter(student_id=student)
    if request.method == "POST":
        feedback = request.POST.get('feedback')

        add_feedback = StudentFeedback(feedback=feedback,student_id=student)
        add_feedback.save()
        messages.success(request, "Feedback Sent Successfully!")
        return redirect('student_feedback')
    else:
        context = {
            "feedback_data":feedback_data
        }
        return render (request, "communication/student_feedback.html", context)

@login_required
def student_feed_reply(request):
    if request.method == "POST":
        feedback_id = request.POST.get('id')
        feedback_reply = request.POST.get('reply')
        feedback = StudentFeedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.save()
        messages.success(request, "Reply Sent Successfully!")
        return redirect('student_feed_reply')

    else:
        feedbacks = StudentFeedback.objects.all()
        context = {
            "feedbacks": feedbacks
        }
    return render(request, 'communication/student_feed_reply.html', context)