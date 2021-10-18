from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from .models import *
from User.models import User, Lecturer, Student
from Classwork.models import *
from Courses import forms
from User.views import CheckValidUser


@CheckValidUser
def UserSchedule(request, id):
    if (request.user.is_lecturer):
        user = Lecturer.objects.get(id=id)
    elif (request.user.is_student):
        user = Student.objects.get(id=id)

    classes = []

    for i in user.class_set.all():
        classes.append(i)

    context = {'classes': classes, 'title': 'Lecturer Schedule'}
    return render(request, 'Courses/schedule.html', context)


@CheckValidUser
def ActiveUserClasses(request, id):
    if (request.user.is_lecturer):
        user = Lecturer.objects.get(id=id)
    elif (request.user.is_student):
        user = Student.objects.get(id=id)

    classes = []

    for i in user.class_set.all():
        classes.append(i)

    context = {'classes': classes}
    return render(request, "Courses/active-classes.html", context)


@CheckValidUser
def UserClassAnnouncement(request, id, class_id):
    announcements = ClassAnnouncement.objects.filter(class_id=class_id).order_by('-time_created')
    user_class = Class.objects.get(id=class_id)
    content = {'user_class': user_class, 'announcements': announcements}
    return render(request, "Courses/class-announcement.html", content)


@CheckValidUser
def UserClassContent(request, id, class_id):
    content_posts = ClassContent.objects.filter(class_id=class_id).order_by('-time_created')
    user_class = Class.objects.get(id=class_id)
    content = {'user_class': user_class, 'content_posts': content_posts}
    return render(request, "Courses/class-content.html", content)


@CheckValidUser
def UserClassGrade(request, id, class_id):
    user_class = Class.objects.get(id=class_id)
    content = {'user_class': user_class}
    return render(request, "Courses/class-grade.html", content)


@CheckValidUser
def UserClassAssignment(request, id, class_id):
    user_class = Class.objects.get(id=class_id)
    tests = user_class.test_set.all()  # lecturers can see all tests
    content = {'user_class': user_class, 'tests': tests}
    return render(request, "Courses/class-assignment.html", content)


def UploadClassAnnouncement(request, id, class_id):
    if request.method == 'POST':
        form = forms.UploadClassAnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.class_id_id = class_id
            announcement.save()
            form.save()
            return HttpResponseRedirect(reverse("user-class-announcement-page", args=[id, class_id]))
    else:
        form = forms.UploadClassAnnouncementForm()
    context = {'form': form, "lecturer": Lecturer.objects.get(id=id), "class": Class.objects.get(id=class_id)}
    return render(request, 'User/upload-announcement.html', context)


def UploadClassContent(request, id, class_id):
    if request.method == 'POST':
        form = forms.UploadClassContentForm(request.POST, request.FILES or None)
        if form.is_valid():
            content = form.save(commit=False)
            content.class_id_id = class_id
            content.save()
            form.save()
            return HttpResponseRedirect(reverse("lecturer-class-content-page", args=[id, class_id]))
    else:
        form = forms.UploadClassContentForm()
    context = {'form': form, "lecturer": Lecturer.objects.get(id=id), "class": Class.objects.get(id=class_id)}
    return render(request, 'User/upload-content.html', context)


def ClassRegistration(request):
    selected_classes_id = []
    if request.method == 'POST':
        selected_classes_id = list(request.POST.keys())[1:]
        selected_classes_id = [int(x) for x in selected_classes_id] # convert to int
    # Selected classes id are in the selected_classes_id list
    available_classes = Class.objects.all()
    context = {'available_classes': available_classes}
    return render(request, 'User/class-registration.html', context)