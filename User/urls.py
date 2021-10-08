from django.urls import path, include
from . import views
from Courses import views as coursesViews

urlpatterns = [
    path('login/',views.LoginView,name="login"),
    path('logout/',views.LogoutView,name="logout"),
    path('<int:id>/about/',views.UserInfoView,name="userinfo"),
    path('student/<int:id>/about/', views.StudentInfoView, name="student-info"),
    path('lecturer/<int:id>/about/', views.LecturerInfoView, name="lecturer-info"),
    path('forgor/', views.PasswordChangeView, name="passwordreset"),
    path('student/<int:id>/announcement/', views.StudentAnnouncement, name="student-announcement-page"),
    path('student/<int:id>/active-courses/', coursesViews.ActiveStudentCourses, name="active-student-courses-page"),
    path('student/<int:id>/calendar/', coursesViews.StudentSchedule, name="student-schedule-page"),
]
