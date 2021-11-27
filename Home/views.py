from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from User.models import User
from User.views import CheckValidUser, fetch_general_announcements
from .models import Announcement


# Decorator to redirect authenticated users
def redirect_auth_user(func):
    def decorate(*args, **kwargs):
        request = args[0]
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            if user.is_student():
                return HttpResponseRedirect(reverse("student-announcement-page", args=[user.student.id]))
            if user.is_lecturer():
                return HttpResponseRedirect(reverse("lecturer-announcement-page", args=[user.lecturer.id]))
        else:
            return func(*args, **kwargs)
    return decorate


# Create your views here.

@redirect_auth_user
def GuestAnnouncement(request):
    return render(request, "User/user-announcement.html",
                  {"general_announcements": fetch_general_announcements()[:7]})


@redirect_auth_user
def GuestAnnouncementAll(request):
    general_announcements = []
    for i in Announcement.objects.all().order_by('-time_created'):
        general_announcements.append(i)
    return render(request, "User/user-general-announcement-view-all.html",
                  {"general_announcements": fetch_general_announcements()})


@redirect_auth_user
def GuestAnnouncementSearch(request):  # new
    query = request.GET.get('search')
    if query is None:
        context = {'announcements': Announcement.objects.order_by("-time_announced")}
        return render(request, "Home/guest-announcement-all.html", context)
    else:
        context = {'announcements': Announcement.objects.filter(title__icontains=query).order_by("-time_announced")}
        return render(request, "Home/guest-announcement-search.html", context)


@redirect_auth_user
def GuestAnnouncementPage(request, id):
    announcement = Announcement.objects.get(id=id)
    return render(request, "User/user-general-announcement-page.html", {"announcement": announcement})


def About(request):
    return render(request, "Home/about.html")


def Talents(request):
    return render(request, "Home/talents.html")


def Contact(request):
    return render(request, "Home/contact.html")
