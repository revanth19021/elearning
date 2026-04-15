from django.shortcuts import render

from django.shortcuts import render, get_object_or_404

from .models import Course, Video


from .models import Course

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


from learning.models import Enrollment

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)

    is_enrolled = Enrollment.objects.filter(
        user=request.user,
        course=course
    ).exists()

    videos = None

    if is_enrolled:
        videos = course.video_set.all()

    return render(request, 'course_detail.html', {
        'course': course,
        'videos': videos,
        'is_enrolled': is_enrolled
    })