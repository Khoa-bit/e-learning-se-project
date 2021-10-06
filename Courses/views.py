from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from User.models import Student

# Create your views here.

'''dummy thoi tu tu them forms and ish do
def ClassRegistration(request):
    classes = Class.objects.all()
    context = {'classes': classes, 'title': 'Class Registration'}
    return render(request, 'Courses/registration.html', context)
'''

def StudentSchedule(request, id):
    user = Student.objects.get(id=id)
    registered_classes = []
    for i in user.class_id.all():
        registered_classes.append(i)
    context = {'registered_classes': registered_classes, 'title': 'Student Schedule'}
    return render(request, 'Courses/schedule.html', context)

def ClassesPage(request, id):
    user = Student.objects.get(id=id)
    registered_classes = []
    for i in user.class_id.all():
        registered_classes.append(i)
    context = {'registered_classes': registered_classes}
    return render(request, 'Courses/registered_classes.html', context)

#def SpecificClass(request, student_id, class_id):
#    return HttpResponse('<h1>ay lmao waddup homie</h1>')