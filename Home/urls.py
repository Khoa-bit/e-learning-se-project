from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.GuestAnnouncement, name="guest-announcement-page"),
    path('user/', include("User.urls")),
    path('announcement/<int:id>', views.GuestAnnouncementPage, name='guest-announcement-viewpage')
]
