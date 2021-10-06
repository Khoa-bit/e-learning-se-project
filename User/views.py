from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from .forms import PasswordResetForm
from django.urls import reverse
from django.contrib import messages


# Create your views here.
def LoginView(request):
  if request.method == "POST":
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request,user)
      if user.is_staff:
        return HttpResponseRedirect(reverse("admin:index"))
      elif user.is_lecturer():
        return HttpResponseRedirect(reverse("lecturerinfo",args=[user.lecturer.id]))
      elif user.is_student():
        return HttpResponseRedirect(reverse("studentinfo",args=[user.student.id]))
      else: return HttpResponseRedirect(reverse("userinfo",args=[user.id]))
  else:
    form = AuthenticationForm()
  return render(request,"User/login.html",{"form":form})

def UserInfoView(request,id):
  user = User.objects.get(id=id)
  if not (request.user.is_authenticated and request.user==user):
    return HttpResponseRedirect(reverse("home"))
  return render(request,"User/userinfo.html")

def LecturerInfoView(request,id):
  user = Lecturer.objects.get(id=id)
  if not (request.user.is_authenticated and request.user==user.user_id):
    return HttpResponseRedirect(reverse("home"))
  return render(request, "User/lecturerinfo.html")
  
def StudentInfoView(request,id):
  user = Student.objects.get(id=id)
  if not (request.user.is_authenticated and request.user==user.user_id):
    return HttpResponseRedirect(reverse("home"))
  return render(request, "User/studentinfo.html")

def PasswordChangeView(request):
  if request.method == "POST":
    form = PasswordResetForm(data=request.POST)
    if form.is_valid():
      data = form.cleaned_data
      if User.objects.filter(email = data["email"]):
        user = User.objects.get(email=data['email'])
        if user.first_name == data['first_name']: 
          user.set_password(data["password"])
          user.save()
          messages.success(request, 'Form submission successful')

  else:
    form = PasswordResetForm()
  return render(request,"User/resetpassword.html",{"form":form})

def UserAnnouncement(request):
  return render(request, "User/user-announcement.html")
