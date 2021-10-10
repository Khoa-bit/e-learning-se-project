from django.contrib import messages
from django.contrib.auth import authenticate, decorators, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import *
from .models import *

# Decorator to check valid user 
def CheckValidUser(func):
  def decorate(*args, **kwargs):
    userID=kwargs['id']
    request = args[0]
    if request.user.is_student():
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
                return HttpResponseRedirect(reverse("student-announcement-page", args=[user.lecturer.id]))
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
def UserInfoView(request, id):
    # user = User.objects.get(id=id)
    # if not (request.user.is_authenticated and request.user == user):
    #     return HttpResponseRedirect(reverse("guest-announcement-page"))
    return render(request, "User/userinfo.html")

@CheckValidUser
def LecturerAboutView(request, id):
    # user = Lecturer.objects.get(id=id)
    # if not (request.user.is_authenticated and request.user == user.user_id):
    #     return HttpResponseRedirect(reverse("guest-announcement-page"))
    return render(request, "User/lecturer-about.html")

@CheckValidUser
def StudentAboutView(request, id):
    # user = Student.objects.get(id=id)
    # user.major_id.name
    # context = {"student": user}
    # if not (request.user.is_authenticated and request.user == user.user_id):
    #     return HttpResponseRedirect(reverse("guest-announcement-page"))
    return render(request, "User/student-about.html", {"student":request.user.student})

@CheckValidUser
def StudentAnnouncement(request, id):
    # user = Student.objects.get(id=id)
    # if not (request.user.is_authenticated and request.user == user.user_id):
    #     return HttpResponseRedirect(reverse("guest-announcement-page"))
    return render(request, "User/student-announcement.html")

def PasswordChangeView(request):
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
    return render(request, "User/resetpassword.html", {"form": form})


def ClassAnnouncement(request):
    form = AnnouncementForm(request.POST)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'User/createannouncement.html', context)
