from django.urls import path

from . import views

app_name = 'enrolments'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.EnrolNewStudentView.as_view(), name='detail'),
    path('<int:pk>/enrolments/', views.EnrolmentsView.as_view(), name='enrolments'),
    path('<int:course_id>/enrol/', views.enrol, name='enrol'),
    path('<int:course_id>/confirmation/<int:student_id>/', views.printEnrolment, name='print-enrolment'),
]