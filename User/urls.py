from django.urls import path, include
from . import views
from Courses import views as coursesViews

urlpatterns = [
    path('login/',views.LoginView,name="login"),
    path('logout/',views.LogoutView,name="logout"),
    path('lecturer/<int:id>/about/', views.LecturerAboutView, name="lecturer-about"),
    path('lecturer/<int:id>/change-password/', views.LecturerChangePassword, name="lecturer-change-password"),
    path('lecturer/<int:id>/announcement/', views.UserAnnouncement, name="lecturer-announcement-page"),
    path('lecturer/<int:id>/active-classes/', coursesViews.ActiveLecturerClasses, name="active-lecturer-classes-page"),
    path('lecturer/<int:id>/calendar/', coursesViews.LecturerSchedule, name="lecturer-schedule-page"),
    path('forgot/', views.ForgotPasswordView, name="forgot-password"),
    path('student/<int:id>/about/', views.StudentAboutView, name="student-about"),
    path('student/<int:id>/change-password/', views.StudentChangePassword, name="student-change-password"),
    path('student/<int:id>/announcement/', views.UserAnnouncement, name="student-announcement-page"),
    path('student/<int:id>/active-classes/', coursesViews.ActiveStudentClasses, name="active-student-classes-page"),
    path('student/<int:id>/calendar/', coursesViews.StudentSchedule, name="student-schedule-page"),
    path('student/<int:id>/registration/', coursesViews.ClassRegistration, name="class-registration-page"),
    path('', include("Courses.urls")),
]
