from django.urls import path, include
from . import views
urlpatterns = [
    path('login/',views.LoginView,name="login"),
    path('<int:id>/about/',views.UserInfoView,name="userinfo"),
    path('student/<int:id>/about/',views.StudentInfoView,name="studentinfo"),
    path('lecturer/<int:id>/about/',views.LecturerInfoView,name="lecturerinfo"),
    path('forgor/',views.PasswordChangeView,name="passwordreset"),
    path('user-announcement/', views.UserAnnouncement, name="user-announcement-page"),
    path('courses/', include('Courses.urls'))
    #path('active-courses/', views.ActiveCourses, name="active-courses-page"),
]
