from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('student/<int:id>/class/<int:class_id>/announcement', views.UserClassAnnouncement, name='user-class-announcement-page'),
    path('student/<int:id>/class/<int:class_id>/content', views.UserClassContent, name='user-class-content-page'),
    path('student/<int:id>/class/<int:class_id>/grade', views.UserClassGrade, name='user-class-grade-page'),
    path('student/<int:id>/class/<int:class_id>/assignment', views.UserClassAssignment, name='user-class-assignment-page'),
    path('registration/', views.ClassRegistration, name='class-registration-page'),
    path('lecturer/<int:id>/class/<int:class_id>/announcement', views.UserClassAnnouncement, name='user-class-announcement-page'),
    path('lecturer/<int:id>/class/<int:class_id>/content', views.UserClassContent, name='user-class-content-page'),
    path('lecturer/<int:id>/class/<int:class_id>/grade', views.UserClassGrade, name='user-class-grade-page'),
    path('lecturer/<int:id>/class/<int:class_id>/assignment', views.UserClassAssignment, name='user-class-assignment-page'),
    path('lecturer/<int:id>/class/<int:class_id>/classwork/',include('Classwork.urls')),
    path('lecturer/<int:id>/class/<int:class_id>/upload-class-announcement/', views.UploadClassAnnouncement, name='upload-class-announcement-page'),
    path('lecturer/<int:id>/class/<int:class_id>/upload-class-content/', views.UploadClassContent, name='upload-class-content-page'),
]
