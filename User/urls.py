from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.LoginView,name="login"),
    path('<int:id>/about/',views.UserInfoView,name="userinfo"),
    path('student/<int:id>/about/',views.StudentInfoView,name="studentinfo"),
    path('lecturer/<int:id>/about/',views.LecturerInfoView,name="lecturerinfo"),
    path('forgor/',views.PasswordChangeView,name="passwordreset"),
]
