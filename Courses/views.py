from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from .models import *
from User.models import Student
from Courses import forms
from User.views import CheckValidUser

# Create your views here.

def ClassRegistration(request):
    pass
@CheckValidUser
def LecturerSchedule(request, id):
    user = Lecturer.objects.get(id=id)
    all_classes = Class.objects.all()
    classes = []

    # if not (request.user.is_authenticated and request.user == user.user_id):
    #     return HttpResponseRedirect(reverse("guest-announcement-page"))

    for i in all_classes:
        if (i.lecturer.user_id == user.user_id):
            classes.append(i)

    context = {'classes': classes, 'title': 'Lecturer Schedule'}
    return render(request, 'Courses/lecturer-schedule.html', context)

@CheckValidUser
def StudentSchedule(request, id):
    user = Student.objects.get(id=id)
    classes = []

    # if not (request.user.is_authenticated and request.user == user.user_id):
    #     return HttpResponseRedirect(reverse("guest-announcement-page"))

    for i in user.class_id.all():
        classes.append(i)

    context = {'classes': classes, 'title': 'Student Schedule'}
    return render(request, 'Courses/student-schedule.html', context)

@CheckValidUser
def ActiveStudentClasses(request, id):
    user = Student.objects.get(id=id)
    classes = []

    # if not (request.user.is_authenticated and request.user == user.user_id):
    #     return HttpResponseRedirect(reverse("guest-announcement-page"))

    for i in user.class_id.all():
        classes.append(i)

    context = {'classes': classes}
    return render(request, "Courses/active-student-classes.html", context)

@CheckValidUser
def ActiveLecturerClasses(request, id):
    all_classes = Class.objects.all()
    user = Lecturer.objects.get(id=id)
    classes = []

    # if not (request.user.is_authenticated and request.user == user.user_id):
    #     return HttpResponseRedirect(reverse("guest-announcement-page"))

    for i in all_classes:
        if (i.lecturer.user_id == user.user_id):
            classes.append(i)

    context = {'classes': classes}
    return render(request, "Courses/active-lecturer-classes.html", context)

@CheckValidUser
def LecturerClassAnnouncement(request, id, class_id):
    # user = Lecturer.objects.get(id=id)
    # if not (request.user.is_authenticated and request.user == user.user_id):
    #     return HttpResponseRedirect(reverse("guest-announcement-page"))

    lecturer_class = Class.objects.get(id=class_id)
    content = {'lecturer_class': lecturer_class}
    return render(request, "Courses/lecturer-class-announcement.html", content)

@CheckValidUser
def StudentClassAnnouncement(request, id, class_id):
    # user = Student.objects.get(id=id)

    # if not (request.user.is_authenticated and request.user == user.user_id):
    #     return HttpResponseRedirect(reverse("guest-announcement-page"))

    student_class = Class.objects.get(id=class_id)
    content = {'student_class': student_class}
    return render(request, "Courses/student-class-announcement.html", content)

@CheckValidUser
def StudentClassContent(request, id, class_id):
    # user = Student.objects.get(id=id)

    # if not (request.user.is_authenticated and request.user == user.user_id):
    #     return HttpResponseRedirect(reverse("guest-announcement-page"))

    student_class = Class.objects.get(id=class_id)
    content = {'student_class': student_class}
    return render(request, "Courses/student-class-content.html", content)

@CheckValidUser
def LecturerClassContent(request, id, class_id):
    # user = Lecturer.objects.get(id=id)

    # if not (request.user.is_authenticated and request.user == user.user_id):
    #     return HttpResponseRedirect(reverse("guest-announcement-page"))

    lecturer_class = Class.objects.get(id=class_id)
    content = {'lecturer_class': lecturer_class}
    return render(request, "Courses/lecturer-class-content.html", content)


def UploadClassAnnouncement(request,id,class_id):
    form = forms.UploadClassAnnouncementForm(request.POST)
    if form.is_valid():
        form.save()
    context = {'form': form,"lecturer":Lecturer.objects.get(id=id),"class":Class.objects.get(id=class_id)}
    return render(request, 'User/upload-announcement.html', context)
