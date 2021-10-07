from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from User.models import User

# Create your views here.

def HomeView(request):
  return render(request, "Home/home.html")

def AboutView(request):
  context={"pageinfo":["DBDUY","SE GROUP","2021"]}
  return render(request, "Home/about.html",context)

def IndexView(request):
  return render(request, "Home/index.html")

def GuestAnnouncement(request):
  if request.user.is_authenticated:
    user = User.objects.get(id=request.user.id)
    if user.is_student():
      return HttpResponseRedirect(reverse("student-announcement-page", args=[user.student.id]))
  return render(request, "Home/guest-announcement.html")