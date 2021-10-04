from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('registration', views.CourseRegistration, name='course-registration'),
    path('timetable', views.Timetable, name='timetable'),
]