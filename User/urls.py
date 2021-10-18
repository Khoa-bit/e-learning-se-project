from django.urls import path, include
from . import views
from Courses import views as coursesViews

urlpatterns = [
    path('login/',views.LoginView,name="login"),
    path('logout/',views.LogoutView,name="logout"),
    path('lecturer/<int:id>/about/', views.LecturerAboutView, name="lecturer-about"),
    path('lecturer/<int:id>/announcement/', views.UserAnnouncement, name="user-announcement-page"),
    path('lecturer/<int:id>/active-classes/', coursesViews.ActiveUserClasses, name="active-user-classes-page"),
    path('lecturer/<int:id>/calendar/', coursesViews.UserSchedule, name="user-schedule-page"),
    path('forgor/', views.PasswordChangeView, name="passwordreset"),
    path('student/<int:id>/about/', views.StudentAboutView, name="student-about"),
    path('student/<int:id>/announcement/', views.UserAnnouncement, name="user-announcement-page"),
    path('student/<int:id>/active-classes/', coursesViews.ActiveUserClasses, name="active-user-classes-page"),
    path('student/<int:id>/calendar/', coursesViews.UserSchedule, name="user-schedule-page"),
    path('student/<int:id>/registration/', coursesViews.ClassRegistration, name="class-registration-page"),
    path('', include("Courses.urls")),
]
