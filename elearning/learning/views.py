from django.shortcuts import redirect
from .models import Enrollment
from courses.models import Course

def enroll(request, course_id):
    course = Course.objects.get(id=course_id)

    Enrollment.objects.get_or_create(
        user=request.user,
        course=course
    )

    return redirect('course_detail', course_id=course.id)