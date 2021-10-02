from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.LoginView,name="login"),
    path('<int:id>/about/',views.UserInfoView,name="userinfo")
]
