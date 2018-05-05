from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Course, Enrolment, Student

import os

class IndexView(generic.ListView):
    template_name = 'enrolments/index.html'
    context_object_name = 'latest_course_list'

    def get_queryset(self):
        """Return the last five published courses."""
        return Course.objects.order_by('-id')[:5]

class DetailView(generic.DetailView):
    model = Course
    template_name = 'enrolments/detail.html'

class EnrolmentsView(generic.ListView):
    template_name = 'enrolments/enrolments.html'
    context_object_name = 'enrolments_list'

    def get_queryset(self):
        return Enrolment.objects.filter(course=self.kwargs['pk'])

def enrol(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    try:
        student = Student.objects.get(pk=request.POST['student'])
    except (KeyError, Student.DoesNotExist):
        return render(request, 'enrolments/detail.html', {
            'course': course,
            'error_message': "Student does not exist."
        })
    else:
        enrolment = Enrolment(course = course, student = student)
        enrolment.save()
        return HttpResponseRedirect(reverse('enrolments:enrolments', args=(course.id,)))
