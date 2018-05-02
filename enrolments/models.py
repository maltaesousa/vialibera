from django.db import models
from django.utils import timezone

class Course(models.Model):
  name = models.TextField()
  description = models.TextField()
  price = models.FloatField()
  datetime_start = models.DateTimeField()
  datetime_end = models.DateTimeField()

class Student(models.Model):
  first_name = models.TextField()
  last_name = models.TextField()
  address = models.TextField()
  zipcode = models.IntegerField()
  city = models.TextField()
  mail = models.EmailField
  phone_number = models.IntegerField()
  birthdate = models.DateField()

class Enrolment(models.Model):
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  paid = models.BooleanField(default=False)
