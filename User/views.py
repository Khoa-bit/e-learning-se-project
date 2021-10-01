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
      return render(request,"User/userinfo.html",{"user":user})
  else:
    form = AuthenticationForm()
  return render(request,"User/login.html",{"form":form})

def UserInfoView(request,id):
  user = User.objects.get(id=id)
  context={"user":user}
  return render(request,"User/userinfo.html",context)