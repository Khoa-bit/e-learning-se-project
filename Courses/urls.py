from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('student/<int:id>/class/<int:class_id>/announcement', views.StudentClassAnnouncement, name='student-class-announcement-page'),
    path('student/<int:id>/class/<int:class_id>/content', views.StudentClassContent, name='student-class-content-page'),
]