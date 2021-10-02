from django.shortcuts import render

# Create your views here.

def HomeView(request):
  return render(request, "Home/home.html")

def AboutView(request):
  context={"pageinfo":["DBDUY","SE GROUP","2021"]}
  return render(request, "Home/about.html",context)