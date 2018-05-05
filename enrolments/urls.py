from django.urls import path

from . import views

app_name = 'enrolments'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/enrolments/', views.ResultsView.as_view(), name='enrolments'),
    path('<int:course_id>/enrol/', views.enrol, name='enrol'),
]