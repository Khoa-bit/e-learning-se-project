from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
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

    if not (request.user.is_authenticated and request.user == user.user_id):
        return HttpResponseRedirect(reverse("guest-announcement-page"))

    for i in user.class_id.all():
        registered_classes.append(i)

    context = {'registered_classes': registered_classes, 'title': 'Student Schedule'}
    return render(request, 'Courses/schedule.html', context)


def ActiveStudentClasses(request, id):
    user = Student.objects.get(id=id)
    registered_classes = []

    if not (request.user.is_authenticated and request.user == user.user_id):
        return HttpResponseRedirect(reverse("guest-announcement-page"))

    for i in user.class_id.all():
        registered_classes.append(i)

    context = {'registered_classes': registered_classes}
    return render(request, "Courses/active-student-courses.html", context)


def StudentClassAnnouncement(request, id, class_id):
    user = Student.objects.get(id=id)

    if not (request.user.is_authenticated and request.user == user.user_id):
        return HttpResponseRedirect(reverse("guest-announcement-page"))

    student_class = Class.objects.get(id=class_id)
    content = {'student_class': student_class}
    return render(request, "Courses/student-class-announcement.html", content)


def StudentClassContent(request, id, class_id):
    user = Student.objects.get(id=id)

    if not (request.user.is_authenticated and request.user == user.user_id):
        return HttpResponseRedirect(reverse("guest-announcement-page"))

    student_class = Class.objects.get(id=class_id)
    content = {'student_class': student_class}
    return render(request, "Courses/student-class-content.html", content)
