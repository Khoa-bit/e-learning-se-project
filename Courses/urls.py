from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path('student/<int:id>/class/<int:class_id>/announcement', views.StudentClassAnnouncement, name='student-class-announcement-page'),
    path('student/<int:id>/class/<int:class_id>/announcement/<int:class_announcement_id>', views.StudentClassAnnouncementViewPage, name="student-class-announcement-viewpage"),
    path('student/<int:id>/class/<int:class_id>/content', views.StudentClassContent, name='student-class-content-page'),
    path('student/<int:id>/class/<int:class_id>/content/<int:content_id>', views.StudentClassContentViewPage, name='student-class-content-view-page'),
    path('student<int:id>/class/<int:class_id>/content/<int:content_id>/download/', views.Download, name='student-download-content'),
    path('student/<int:id>/class/<int:class_id>/grade', views.StudentClassGrade, name='student-class-grade-page'),
    path('student/<int:id>/class/<int:class_id>/assignment', views.StudentClassAssignment, name='student-class-assignment-page'),
    path('student/<int:id>/registration', views.ClassRegistration, name='student-class-registration-page'),
    path('student/<int:id>/edit-registration', views.EditClassRegistration, name='edit-class-registration-page'),
    path('student/<int:id>/class/<int:class_id>/staff-contact/', views.StaffContact, name='student-staff-contact-page'),
    path('student/<int:id>/class/<int:class_id>/classwork/',include('Classwork.urls')),
    path('student/<int:id>/class/<int:class_id>/performance', views.ViewSelfCoursePerformance, name='student-view-self-course-performance'),
    path('lecturer/<int:id>/class/<int:class_id>/announcement', views.LecturerClassAnnouncement, name='lecturer-class-announcement-page'),
    path('lecturer/<int:id>/class/<int:class_id>/announcement/<int:class_announcement_id>', views.LecturerClassAnnouncementViewPage, name="lecturer-class-announcement-viewpage"),
    path('lecturer/<int:id>/class/<int:class_id>/content', views.LecturerClassContent, name='lecturer-class-content-page'),
    path('lecturer/<int:id>/class/<int:class_id>/content/<int:content_id>', views.LecturerClassContentViewPage, name='lecturer-class-content-view-page'),
    path('lecturer<int:id>/class/<int:class_id>/content/<int:content_id>/download/', views.Download, name='lecturer-download-content'),
    path('lecturer/<int:id>/class/<int:class_id>/classwork/',include('Classwork.urls')),
    path('lecturer/<int:id>/class/<int:class_id>/grade', views.LecturerClassGrade, name='lecturer-class-grade-page'),
    path('lecturer/<int:id>/class/<int:class_id>/assignment', views.LecturerClassAssignment, name='lecturer-class-assignment-page'),
    path('lecturer/<int:id>/class/<int:class_id>/upload-class-announcement/', views.UploadClassAnnouncement, name='upload-class-announcement-page'),
    path('lecturer/<int:id>/class/<int:class_id>/upload-class-content/', views.UploadClassContent, name='upload-class-content-page'),
    path('lecturer/<int:id>/class/<int:class_id>/staff-contact/', views.StaffContact, name='lecturer-staff-contact-page'),
    path('lecturer/<int:id>/class/<int:class_id>/student-list/', views.ViewStudentList, name='lecturer-class-view-student-list'),
    path('lecturer/<int:id>/class/<int:class_id>/student/<int:student_id>/performance', views.ViewStudentCoursePerformance, name='lecturer-view-student-course-performance'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)

