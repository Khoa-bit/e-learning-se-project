from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('student/<int:id>/class/<int:class_id>/announcement', views.StudentClassAnnouncement, name='student-class-announcement-page'),
    path('student/<int:id>/class/<int:class_id>/content', views.StudentClassContent, name='student-class-content-page'),
    path('student/<int:id>/class/<int:class_id>/grade', views.StudentClassGrade, name='student-class-grade-page'),
    path('student/<int:id>/class/<int:class_id>/assignment', views.StudentClassAssignment, name='student-class-assignment-page'),
    path('student/<int:id>/registration', views.ClassRegistration, name='student-class-registration-page'),
    path('student/<int:id>/edit-registration', views.EditClassRegistration, name='edit-class-registration-page'),
    path('lecturer/<int:id>/class/<int:class_id>/announcement', views.LecturerClassAnnouncement, name='lecturer-class-announcement-page'),
    path('lecturer/<int:id>/class/<int:class_id>/content', views.LecturerClassContent, name='lecturer-class-content-page'),
    path('lecturer/<int:id>/class/<int:class_id>/classwork/',include('Classwork.urls')),
    path('student/<int:id>/class/<int:class_id>/classwork/',include('Classwork.urls')),
    path('lecturer/<int:id>/class/<int:class_id>/grade', views.LecturerClassGrade, name='lecturer-class-grade-page'),
    path('lecturer/<int:id>/class/<int:class_id>/assignment', views.LecturerClassAssignment, name='lecturer-class-assignment-page'),
    path('lecturer/<int:id>/class/<int:class_id>/upload-class-announcement/', views.UploadClassAnnouncement, name='upload-class-announcement-page'),
    path('lecturer/<int:id>/class/<int:class_id>/upload-class-content/', views.UploadClassContent, name='upload-class-content-page'),
]
