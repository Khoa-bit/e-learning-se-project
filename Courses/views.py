from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import *
from User.models import Student
from Classwork.models import *
from Courses import forms
from User.views import CheckValidUser


@CheckValidUser
def LecturerSchedule(request, id):
    user = Lecturer.objects.get(id=id)
    classes = []

    for i in user.class_set.all():
        classes.append(i)

    context = {'classes': classes, 'title': 'Lecturer Schedule'}
    return render(request, 'Courses/schedule.html', context)


@CheckValidUser
def StudentSchedule(request, id):
    user = Student.objects.get(id=id)
    classes = []

    for i in user.class_id.all():
        classes.append(i)

    context = {'classes': classes, 'title': 'Student Schedule'}
    return render(request, 'Courses/schedule.html', context)


@CheckValidUser
def ActiveStudentClasses(request, id):
    user = Student.objects.get(id=id)
    classes = []

    for i in user.class_id.all():
        classes.append(i)

    context = {'classes': classes}
    return render(request, "Courses/active-classes.html", context)


@CheckValidUser
def ActiveLecturerClasses(request, id):
    user = Lecturer.objects.get(id=id)
    classes = []

    for i in user.class_set.all():
        classes.append(i)

    context = {'classes': classes}
    return render(request, "Courses/active-classes.html", context)


@CheckValidUser
def LecturerClassAnnouncement(request, id, class_id):
    user = Lecturer.objects.get(id=id)
    if (class_id not in user.class_set.all().values_list('id', flat=True)):
        return HttpResponseRedirect(reverse("lecturer-announcement-page", args=[id]))
    announcements = ClassAnnouncement.objects.filter(class_id=class_id).order_by('-time_created')
    lecturer_class = Class.objects.get(id=class_id)
    content = {'lecturer_class': lecturer_class, 'announcements': announcements}
    return render(request, "Courses/class-announcement.html", content)


@CheckValidUser
def StudentClassAnnouncement(request, id, class_id):
    announcements = ClassAnnouncement.objects.filter(class_id=class_id).order_by('-time_created')
    student_class = Class.objects.get(id=class_id)
    content = {'student_class': student_class, 'announcements': announcements}
    return render(request, "Courses/class-announcement.html", content)


@CheckValidUser
def StudentClassContent(request, id, class_id):
    content_posts = ClassContent.objects.filter(class_id=class_id).order_by('-time_created')
    student_class = Class.objects.get(id=class_id)
    content = {'student_class': student_class, 'content_posts': content_posts}
    return render(request, "Courses/class-content.html", content)


@CheckValidUser
def LecturerClassContent(request, id, class_id):
    user = Lecturer.objects.get(id=id)
    if (class_id not in user.class_set.all().values_list('id', flat=True)):
        return HttpResponseRedirect(reverse("lecturer-announcement-page", args=[id]))
    content_posts = ClassContent.objects.filter(class_id=class_id).order_by('-time_created')
    lecturer_class = Class.objects.get(id=class_id)
    content = {'lecturer_class': lecturer_class, 'content_posts': content_posts}
    return render(request, "Courses/class-content.html", content)


@CheckValidUser
def StudentClassAssignment(request, id, class_id):
    student_class = Class.objects.get(id=class_id)
    test = student_class.test_set.all()     # add filter here (check if test is in the time window because students can only see those tests)
    content = {'student_class': student_class,'tests':test}
    return render(request, "Courses/class-assignment.html", content)


@CheckValidUser
def LecturerClassAssignment(request, id, class_id):
    user = Lecturer.objects.get(id=id)
    if (class_id not in user.class_set.all().values_list('id', flat=True)):
        return HttpResponseRedirect(reverse("lecturer-announcement-page", args=[id]))
    lecturer_class = Class.objects.get(id=class_id)
    tests = lecturer_class.test_set.all()   # lecturers can see all tests
    content = {'lecturer_class': lecturer_class, 'tests':tests}
    return render(request, "Courses/class-assignment.html", content)


@CheckValidUser
def StudentClassGrade(request, id, class_id):
    student_class = Class.objects.get(id=class_id)
    content = {'student_class': student_class}
    return render(request, "Courses/class-grade.html", content)


@CheckValidUser
def LecturerClassGrade(request, id, class_id):
    user = Lecturer.objects.get(id=id)
    if (class_id not in user.class_set.all().values_list('id', flat=True)):
        return HttpResponseRedirect(reverse("lecturer-announcement-page", args=[id]))
    lecturer_class = Class.objects.get(id=class_id)
    content = {'lecturer_class': lecturer_class}
    return render(request, "Courses/class-grade.html", content)


@CheckValidUser
def UploadClassAnnouncement(request, id, class_id):
    if request.method == 'POST':
        form = forms.UploadClassAnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.class_id_id = class_id
            announcement.save()
            form.save()
            return HttpResponseRedirect(reverse("lecturer-class-announcement-page", args=[id, class_id]))
    else:
        form = forms.UploadClassAnnouncementForm()
    context = {'form': form, "lecturer": Lecturer.objects.get(id=id), "class": Class.objects.get(id=class_id)}
    return render(request, 'User/upload-announcement.html', context)


@CheckValidUser
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


@CheckValidUser
def ClassRegistration(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = forms.ClassRegistrationForm()
        selected_classes = request.POST.getlist('selection')
        for i in selected_classes:
            student.class_id.add(i)
        return HttpResponseRedirect(reverse('student-class-registration-page', args=[id]))
    else:
        form = forms.ClassRegistrationForm()
    context = {'form': form}
    return render(request, 'User/class-registration.html', context)


