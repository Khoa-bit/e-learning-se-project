from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.HomeView,name="home"),
    path('user/',include("User.urls")),
    path('about/',views.AboutView,name="about-page")
]
