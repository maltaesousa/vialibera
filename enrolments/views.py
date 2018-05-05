from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import HttpResponse

from .models import Course, Enrolment, Student

import os

def index(request):
    latest_course_list = Course.objects.order_by('-id')[:5]
    context = {
        'latest_course_list': latest_course_list
    }
    return render(request, 'enrolments/index.html', context)

def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'enrolments/detail.html', {'course': course})

def enrolments(request, course_id):
    enrolments_list = get_list_or_404(Enrolment, course_id=course_id)
    return render(request, 'enrolments/enrolments.html', {'enrolments_list': enrolments_list})

def enrol(request, course_id):
    return render(request, 'enrolments/enrol.html', {})
