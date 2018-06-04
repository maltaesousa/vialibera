from django import forms
from .models import Student, Enrolment


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class EnrolForm(forms.ModelForm):
    class Meta:
        model = Enrolment
        fields = '__all__'
