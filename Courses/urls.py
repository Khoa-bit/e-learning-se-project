from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.lmao, name='lmao'),
    #path('registration', views.ClassRegistration, name='class-registration'),
    path('<int:id>/timetable', views.StudentSchedule, name='student-timetable'),
    path('<int:id>/classes', views.CoursesPage, name='student-classes')
]