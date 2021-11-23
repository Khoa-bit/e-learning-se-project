from django.contrib import messages
from django.contrib.auth import authenticate, decorators, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import *
from .models import *
from Courses.models import ClassAnnouncement
from Home.models import Announcement

# Decorator to check valid user


def CheckValidUser(func):
    def decorate(*args, **kwargs):
        userID = kwargs['id']
        request = args[0]
        if request.user.id==None:
            return HttpResponseRedirect(reverse("login"))
        elif request.user.is_student():
            user = Student.objects.get(id=userID).user_id
        elif request.user.is_lecturer():
            user = Lecturer.objects.get(id=userID).user_id
        else:
            user = User.objects.get(id=userID)
        if request.user == user and request.user.is_authenticated:
            return func(*args, **kwargs)
        else:
            return HttpResponseRedirect(reverse("guest-announcement-page"))
    return decorate

# Create your views here.


def LoginView(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_staff:
                return HttpResponseRedirect(reverse("admin:index"))
            elif user.is_lecturer():
                return HttpResponseRedirect(reverse("lecturer-announcement-page", args=[user.lecturer.id]))
            elif user.is_student():
                return HttpResponseRedirect(reverse("student-announcement-page", args=[user.student.id]))
            else:
                return HttpResponseRedirect(reverse("userinfo", args=[user.id]))
    else:
        form = LoginForm()
    return render(request, "User/login.html", {"form": form})


def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse("guest-announcement-page"))


@CheckValidUser
def LecturerAboutView(request, id):
    return render(request, "User/user-about.html", {"userObj": Lecturer.objects.get(id=id.user_id)})


@CheckValidUser
def StudentAboutView(request, id):
    return render(request, "User/user-about.html", {"userObj": Student.objects.get(id=id).user_id})


@CheckValidUser
def StudentUserAnnouncement(request, id):
    student = Student.objects.get(id=id)
    class_announcements = []
    general_announcements = []
    for i in Announcement.objects.all().order_by('-time_created'):
        general_announcements.append(i)
    for class_id in student.class_id.all():
        for announcement in ClassAnnouncement.objects.filter(class_id=class_id).order_by("-time_created"):
            class_announcements.append(announcement)
    return render(request, "User/user-announcement.html", {"class_announcements": class_announcements[:3], "general_announcements": general_announcements[:3]})


@CheckValidUser
def LecturerUserAnnouncement(request, id):
    lecturer = Lecturer.objects.get(id=id)
    class_announcements = []
    general_announcements = []
    for i in Announcement.objects.all().order_by('-time_created'):
        general_announcements.append(i)
    for class_id in lecturer.class_set.all():
        for announcement in ClassAnnouncement.objects.filter(class_id=class_id).order_by("-time_created"):
            class_announcements.append(announcement)
    return render(request, "User/user-announcement.html", {"class_announcements": class_announcements, "general_announcements": general_announcements[:3]})


@CheckValidUser
def StudentGeneralAnnouncementViewAll(request, id):
    general_announcements = []
    for i in Announcement.objects.all().order_by('-time_created'):
        general_announcements.append(i)
    return render(request, "User/user-general-announcement-view-all.html", {"general_announcements": general_announcements})


@CheckValidUser
def LecturerGeneralAnnouncementViewAll(request, id):
    general_announcements = []
    for i in Announcement.objects.all().order_by('-time_created'):
        general_announcements.append(i)
    return render(request, "User/user-general-announcement-view-all.html", {"general_announcements": general_announcements})


@CheckValidUser
def StudentClassAnnouncementViewAll(request, id):
    student = Student.objects.get(id=id)
    class_announcements = []
    for class_id in student.class_id.all():
        for announcement in ClassAnnouncement.objects.filter(class_id=class_id).order_by("-time_created"):
            class_announcements.append(announcement)
    return render(request, "User/user-class-announcement-view-all.html", {"class_announcements": class_announcements})


@CheckValidUser
def LecturerClassAnnouncementViewAll(request, id):
    lecturer = Lecturer.objects.get(id=id)
    class_announcements = []
    for class_id in lecturer.class_set.all():
        for announcement in ClassAnnouncement.objects.filter(class_id=class_id).order_by("-time_created"):
            class_announcements.append(announcement)
    return render(request, "User/user-class-announcement-view-all.html", {"class_announcements": class_announcements})


@CheckValidUser
def StudentClassAnnouncementPage(request, id, class_id, class_announcement_id):
    announcement = ClassAnnouncement.objects.get(id=class_announcement_id)
    return render(request, "User/user-class-announcement-page.html", {"announcement": announcement})


@CheckValidUser
def LecturerClassAnnouncementPage(request, id, class_id, class_announcement_id):
    announcement = ClassAnnouncement.objects.get(id=class_announcement_id)
    return render(request, "User/user-class-announcement-page.html", {"announcement": announcement})


@CheckValidUser
def StudentGeneralAnnouncementPage(request, id, announcement_id):
    announcement = Announcement.objects.get(id=announcement_id)
    return render(request, "User/user-general-announcement-page.html", {"announcement": announcement})


@CheckValidUser
def LecturerGeneralAnnouncementPage(request, id, announcement_id):
    announcement = Announcement.objects.get(id=announcement_id)
    return render(request, "User/user-general-announcement-page.html", {"announcement": announcement})


def ForgotPasswordView(request):
    if request.method == "POST":
        form = PasswordResetForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if User.objects.filter(email=data["email"]):
                user = User.objects.get(email=data['email'])
                if user.first_name == data['first_name']:
                    user.set_password(data["password"])
                    user.save()
                    messages.success(request, 'Form submission successful')
    else:
        form = PasswordResetForm()
    return render(request, "User/forgot-password.html", {"form": form})


def StudentChangePassword(request, id):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('student-change-password',request.user.student.id)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "User/change-password.html", {'form': form,'student':request.user.student})
    #return render(request, "User/change-password.html", {"student": request.user.student})


def LecturerChangePassword(request, id):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('lecturer-change-password',request.user.lecturer.id)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "User/change-password.html", {'form': form,'lecturer':request.user.lecturer})
    #return render(request, "User/change-password.html", {"lecturer": request.user.lecturer})
