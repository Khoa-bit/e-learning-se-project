from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.GuestAnnouncement, name="guest-announcement-page"),
    path('user/', include("User.urls")),
    path('announcement/<int:id>', views.GuestAnnouncementPage, name='guest-announcement-viewpage'),
    path('about/', views.GuestAbout, name='guest-about'),
    path('contact-us/', views.Contact, name='contact'),
    path('announcement/all/', views.GuestAnnouncementAll, name='guest-announcement-all'),
    path('announcement/search/', views.GuestAnnouncementSearch, name='guest-announcement-search'),
]
