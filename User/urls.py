from django.urls import path, include
from . import views
from Courses import views as coursesViews

urlpatterns = [
    path('login/',views.LoginView,name="login"),
    path('logout/',views.LogoutView,name="logout"),
    path('<int:id>/about/',views.UserInfoView,name="userinfo"),
    path('student/<int:id>/about/', views.StudentAboutView, name="student-about"),
    path('lecturer/<int:id>/about/', views.LecturerInfoView, name="lecturer-about"),
    path('lecturer/<int:id>/active-classes/', coursesViews.ActiveLecturerClasses, name="active-lecturer-classes-page"),
    path('forgor/', views.PasswordChangeView, name="passwordreset"),
    path('student/<int:id>/announcement/', views.StudentAnnouncement, name="student-announcement-page"),
    path('student/<int:id>/active-classes/', coursesViews.ActiveStudentClasses, name="active-student-classes-page"),
    path('student/<int:id>/calendar/', coursesViews.StudentSchedule, name="student-schedule-page"),
    path('student/<int:id>/registration/', coursesViews.ClassRegistration, name="class-registration-page"),
    path('lecturer/<int:id>/create-class-announcement/', views.ClassAnnouncement, name = 'class-announcement-creation'),
    #path('', include("Courses.urls")),
    path('student/<int:id>', include("Courses.urls")),
    path('lecturer/<int:id>', include("Courses_Lecturer.urls")),
]
