from django.contrib import admin
from .models import Course, Student, Enrolment

admin.site.register([Course, Student, Enrolment])