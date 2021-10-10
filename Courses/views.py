from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from .models import *
from User.models import Student

# Create your views here.

def ClassRegistration(request):
    pass


def StudentSchedule(request, id):
    user = Student.objects.get(id=id)
    classes = []

    if not (request.user.is_authenticated and request.user == user.user_id):
        return HttpResponseRedirect(reverse("guest-announcement-page"))

    for i in user.class_id.all():
        classes.append(i)

    context = {'classes': classes, 'title': 'Student Schedule'}
    return render(request, 'Courses/schedule.html', context)


def ActiveStudentClasses(request, id):
    user = Student.objects.get(id=id)
    classes = []

    if not (request.user.is_authenticated and request.user == user.user_id):
        return HttpResponseRedirect(reverse("guest-announcement-page"))

    for i in user.class_id.all():
        classes.append(i)

    context = {'classes': classes}
    return render(request, "Courses/active-student-classes.html", context)

def ActiveLecturerClasses(request, id):
    all_classes = Class.objects.all()
    user = Lecturer.objects.get(id=id)
    classes = []

    if not (request.user.is_authenticated and request.user == user.user_id):
        return HttpResponseRedirect(reverse("guest-announcement-page"))

    for i in all_classes:
        if (i.lecturer.user_id == user.user_id):
            classes.append(i)

    context = {'classes': classes}
    return render(request, "Courses/active-lecturer-classes.html", context)

def LecturerClassAnnouncement(request, id, class_id):
    user = Student.objects.get(id=id)

    if not (request.user.is_authenticated and request.user == user.user_id):
        return HttpResponseRedirect(reverse("guest-announcement-page"))

    class_id = Class.objects.get(id=class_id)
    content = {'class_id': class_id}
    return render(request, "Courses/lecturer-class-announcement.html", content)


def StudentClassAnnouncement(request, id, class_id):
    user = Student.objects.get(id=id)

    if not (request.user.is_authenticated and request.user == user.user_id):
        return HttpResponseRedirect(reverse("guest-announcement-page"))

    class_id = Class.objects.get(id=class_id)
    content = {'class_id': class_id}
    return render(request, "Courses/student-class-announcement.html", content)


def StudentClassContent(request, id, class_id):
    user = Student.objects.get(id=id)

    if not (request.user.is_authenticated and request.user == user.user_id):
        return HttpResponseRedirect(reverse("guest-announcement-page"))

    classes = Class.objects.get(id=class_id)
    content = {'classes': classes}
    return render(request, "Courses/student-class-content.html", content)
