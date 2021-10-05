from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.lmao, name='lmao'),
    path('registration', views.ClassRegistration, name='class-registration'),
    path('timetable', views.StudentSchedule, name='student-timetable'),
]