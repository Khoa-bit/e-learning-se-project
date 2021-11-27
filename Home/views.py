from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from User.models import User
from User.views import CheckValidUser
from .models import Announcement

# Create your views here.

def HomeView(request):
  return render(request, "Home/home.html")


def GuestAnnouncement(request):
    '''
    context = {'announcements' : Announcement.objects.order_by("-time_announced")[:5]}
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        if user.is_student():
            return HttpResponseRedirect(reverse("student-announcement-page", args=[user.student.id]))
        if user.is_lecturer():
            return HttpResponseRedirect(reverse("lecturer-announcement-page", args=[user.lecturer.id]))
    '''
    general_announcements = []
    for i in Announcement.objects.all().order_by('-time_created'):
        general_announcements.append(i)
    return render(request, "User/user-announcement.html", {"general_announcements": general_announcements[:3]})


def GuestAnnouncementAll(request):
    '''
    context = {'announcements' : Announcement.objects.order_by("-time_announced")}
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        if user.is_student():
            return HttpResponseRedirect(reverse("student-announcement-page", args=[user.student.id]))
        if user.is_lecturer():
            return HttpResponseRedirect(reverse("lecturer-announcement-page", args=[user.lecturer.id]))
    '''
    general_announcements = []
    for i in Announcement.objects.all().order_by('-time_created'):
        general_announcements.append(i)
    return render(request, "User/user-general-announcement-view-all.html", {"general_announcements": general_announcements})


def GuestAnnouncementSearch(request): # new
        query = request.GET.get('search')
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            if user.is_student():
                return HttpResponseRedirect(reverse("student-announcement-page", args=[user.student.id]))
            if user.is_lecturer():
                return HttpResponseRedirect(reverse("lecturer-announcement-page", args=[user.lecturer.id]))
        if query is None:
            context = {'general_announcements' : Announcement.objects.order_by("-time_created")}
            return render(request, "User/user-general-announcement-view-all.html", context)
        else:
            context = {'general_announcements': Announcement.objects.filter(title__icontains=query).order_by("-time_created")}
            return render(request, "User/user-general-announcement-view-all.html", context)


def GuestAnnouncementPage(request, id):
    #announcement = Announcement.objects.get(id=id)
    context = {'announcements' : Announcement.objects.filter(id=id)}
    return render(request, "User/user-general-announcement-page.html", context)


def GuestAbout(request):
    return render(request, "Home/about.html")


def Contact(request):
    return render(request, "Home/contact.html")
