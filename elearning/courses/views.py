from django.shortcuts import render

from django.shortcuts import render, get_object_or_404

from .models import Course, Video


def course_list(request):
    return render(request, 'course_list.html')


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    videos = Video.objects.filter(course=course)

    return render(request, 'course_detail.html', {
        'course': course,
        'videos': videos
    })