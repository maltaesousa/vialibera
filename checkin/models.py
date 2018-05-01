from django.db import models

class Course(models.Model):
  name = models.TextField
  description = models.TextField
  price = models.FloatField
  date_start = models.DateTimeField
  date_ends = models.DateTimeField

class Student(models.Model):
  firstname = models.TextField
  lastname = models.TextField
  post_address = models.TextField
  post_code = models.IntegerField
  post_town = models.TextField
  email = models.EmailField
  phone = models.IntegerField
  birthdate = models.DateField

class Enrolment(models.Model):
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  paid = models.BooleanField
