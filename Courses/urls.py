from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('registration', views.ClassRegistration, name='class-registration'),
    path('<int:id>/schedule', views.StudentSchedule, name='student-timetable'),
    # path('<int:id>/classes', views.ClassesPage, name='student-classes'),
    #path('<int:id>/<int:id>', views.SpecificClass, name='specific-classes')
    path('student/<int:id>/active-courses/', views.ActiveStudentCourses, name="active-student-courses-page"),
]