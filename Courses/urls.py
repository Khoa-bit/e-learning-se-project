from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('student/<int:id>/class/<int:class_id>/announcement', views.StudentClassAnnouncement, name='student-class-announcement-page'),
    #path('student/<int:id>/class/<int:class_id>/content', views.StudentClassContent, name='student-class-content-page'),
    path('announcement/', views.StudentClassAnnouncement, name='class-announcement-page')
    path('content/', views.StudentClassContent, name='class-content-page')
]
