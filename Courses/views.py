from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def lmao(request):
    return HttpResponse("<h1>ay lmao you're in courses</h1>")

# dummy thoi tu tu them forms and ish do
def ClassRegistration(request):
    classes = Class.objects.all()
    context = {'classes': classes, 'title': 'Class Registration'}
    return render(request, 'Courses/registration.html', context)

# gonna have reference to registered classes later
def StudentSchedule(request):
    schedules = Timetable.objects.all()
    context = {'schedules': schedules, 'title': 'Student Schedule'}
    return render(request, 'Courses/timetable.html', context)