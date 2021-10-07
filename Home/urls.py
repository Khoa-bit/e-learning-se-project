from . import views
from django.urls import path,include

urlpatterns = [
    # path('',views.HomeView,name="home"),
    path('',views.GuestAnnouncement,name="guest-announcement-page"),
    path('user/',include("User.urls")),
    path('about/',views.AboutView,name="about-page"),
    path('index/',views.IndexView,name="index-page"),
]

