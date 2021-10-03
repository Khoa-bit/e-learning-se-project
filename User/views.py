from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse


# Create your views here.
def LoginView(request):
  if request.method == "POST":
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request,user)
      if user.is_staff:
        return HttpResponseRedirect(reverse("admin:index"))
      return HttpResponseRedirect(reverse("userinfo",args=[user.id]))
  else:
    form = AuthenticationForm()
  return render(request,"User/login.html",{"form":form})

def UserInfoView(request,id):
  user = User.objects.get(id=id)
  if not (request.user.is_authenticated and request.user==user):
    return HttpResponseRedirect(reverse("home"))
  context={"user":user}
  if hasattr(user,"student"):
    context["role"]="student"
  elif hasattr(user,"lecturer"): context["role"]="Lecturer"
  else: context["role"]="user"
  print(context)
  return render(request,"User/userinfo.html",context)

