from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from User.models import Student

# Create your views here.
def lmao(request):
    return HttpResponse("<h1>ay lmao you're in courses</h1>")

'''dummy thoi tu tu them forms and ish do
def ClassRegistration(request):
    classes = Class.objects.all()
    context = {'classes': classes, 'title': 'Class Registration'}
    return render(request, 'Courses/registration.html', context)
'''

# gonna have reference to registered classes later
def StudentSchedule(request, id):
    user = Student.objects.get(id=id)
    schedules = Timetable.objects.all()
    context = {'schedules': schedules, 'title': 'Student Schedule'}
    return render(request, 'Courses/timetable.html', context)

def CoursesPage(request, id):
    #try:
    #except Student.DoesNotExist:
    #    user = None

    user = Student.objects.get(id=id)
    courses = []
    for i in user.class_id.all():
        courses.append(i)
    context = {'courses': courses}
    return render(request, 'Courses/courses.html', context)