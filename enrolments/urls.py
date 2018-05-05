from django.urls import path

from . import views

app_name = 'enrolments'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>/', views.detail, name='detail'),
    path('<int:course_id>/enrolments/', views.enrolments, name='enrolments'),
    path('<int:course_id>/enrol/', views.enrol, name='enrol'),
]