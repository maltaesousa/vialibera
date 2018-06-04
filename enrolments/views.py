from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .forms import CreateStudentForm
from .models import Course, Enrolment, Student

from reportlab.pdfgen import canvas

class IndexView(generic.ListView):
    template_name = 'enrolments/index.html'
    context_object_name = 'latest_course_list'

    def get_queryset(self):
        """Return the last five published courses."""
        return Course.objects.order_by('-id')[:5]


class EnrolNewStudentView(generic.DetailView):
    model = Course
    form = CreateStudentForm()
    template_name = 'enrolments/detail.html'
    extra_context = { 'form': form }


class EnrolmentsView(generic.ListView):
    template_name = 'enrolments/enrolments.html'
    context_object_name = 'enrolments_list'

    def get_queryset(self):
        return Enrolment.objects.filter(course=self.kwargs['pk'])


def enrol(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    form = CreateStudentForm(request.POST)
    new_student = form.save()
    new_enrolment = Enrolment(course=course, student= new_student)
    new_enrolment.save()
    student_id = new_student.id
    return HttpResponseRedirect(reverse('enrolments:print-enrolment', args=(course.id, student_id)))


def printEnrolment(request, course_id, student_id):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Confirmation.pdf"'

    p = canvas.Canvas(response)
    course = get_object_or_404(Course, pk=course_id)
    student = get_object_or_404(Student, pk=student_id)
    p.drawString(100, 750, "Confirmation d'inscription")
    p.drawString(100, 700, "Étudiant: " + student.first_name + ' ' + student.last_name)
    p.drawString(100, 650, "Cours: " + course.name)
    p.drawString(100, 600, "Veuillez vous aquiter de la somme au début du cours.")

    p.showPage()
    p.save()
    #TODO redirect!
    return response