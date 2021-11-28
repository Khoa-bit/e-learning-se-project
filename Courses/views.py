import os
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone

from .models import *
from User.models import Student, Lecturer
from Classwork.models import *
from Courses import forms
from User.views import CheckValidUser
from datetime import datetime
from django.conf import Settings, settings
from django.http import HttpResponse, Http404
from django.views.static import serve



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


def fetch_class_announcements(class_id):
    class_announcements = []
    for announcement in ClassAnnouncement.objects.filter(class_id=class_id).order_by("-time_modified"):
        is_new = timezone.now() - announcement.time_modified < timezone.timedelta(weeks=1)
        class_announcements.append({"obj": announcement, "is_new": is_new})
    return class_announcements


@CheckValidUser
def LecturerClassAnnouncement(request, id, class_id):
    lecturer = Lecturer.objects.get(id=id)
    if (class_id not in lecturer.class_set.all().values_list('id', flat=True)):
        return HttpResponseRedirect(reverse("lecturer-announcement-page", args=[id]))
    class_announcements = fetch_class_announcements(class_id)
    lecturer_class = Class.objects.get(id=class_id)
    content = {'lecturer_class': lecturer_class, 'class_announcements': class_announcements}
    return render(request, "Courses/class-announcement.html", content)


@CheckValidUser
def StudentClassAnnouncement(request, id, class_id):
    class_announcements = fetch_class_announcements(class_id)
    student_class = Class.objects.get(id=class_id)
    content = {'student_class': student_class, 'class_announcements': class_announcements}
    return render(request, "Courses/class-announcement.html", content)


def fetch_class_content_posts(class_id):
    class_content_posts = []
    for content_post in ClassContent.objects.filter(class_id=class_id).order_by('-time_modified'):
        is_new = timezone.now() - content_post.time_modified < timezone.timedelta(weeks=1)
        class_content_posts.append({"obj": content_post, "is_new": is_new})
    return class_content_posts


@CheckValidUser
def StudentClassAnnouncementViewPage(request, id, class_id, class_announcement_id):
    announcement = ClassAnnouncement.objects.get(id=class_announcement_id)
    return render(request, "Courses/class-announcement-viewpage.html", {"announcement": announcement})


@CheckValidUser
def LecturerClassAnnouncementViewPage(request, id, class_id, class_announcement_id):
    announcement = ClassAnnouncement.objects.get(id=class_announcement_id)
    return render(request, "Courses/class-announcement-viewpage.html", {"announcement": announcement})


@CheckValidUser
def StudentClassContent(request, id, class_id):
    content_posts = fetch_class_content_posts(class_id)
    student_class = Class.objects.get(id=class_id)
    content = {'student_class': student_class, 'content_posts': content_posts}
    return render(request, "Courses/class-content.html", content)


@CheckValidUser
def LecturerClassContent(request, id, class_id):
    user = Lecturer.objects.get(id=id)
    if (class_id not in user.class_set.all().values_list('id', flat=True)):
        return HttpResponseRedirect(reverse("lecturer-announcement-page", args=[id]))
    content_posts = fetch_class_content_posts(class_id)
    lecturer_class = Class.objects.get(id=class_id)
    content = {'lecturer_class': lecturer_class, 'content_posts': content_posts}
    return render(request, "Courses/class-content.html", content)


@CheckValidUser
def StudentClassContentViewPage(request, id, class_id, content_id):
    content_post = ClassContent.objects.get(id=content_id)
    return render(request, "Courses/class-content-viewpage.html", {"content_post": content_post, "id": id, "class_id": class_id})


@CheckValidUser
def LecturerClassContentViewPage(request, id, class_id, content_id):
    content_post = ClassContent.objects.get(id=content_id)
    return render(request, "Courses/class-content-viewpage.html", {"content_post": content_post, "id": id, "class_id": class_id})


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
    context = {'form': form, "lecturer": Lecturer.objects.get(id=id), "lecturer_class": Class.objects.get(id=class_id)}
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
    context = {'form': form, "lecturer": Lecturer.objects.get(id=id), "lecturer_class": Class.objects.get(id=class_id)}
    return render(request, 'User/upload-content.html', context)


@CheckValidUser
def Download(request, id, class_id, content_id):
    content = ClassContent.objects.get(id=content_id)
    path = content.attached_file.url
    file_path = str(settings.BASE_DIR).replace("\\","/")+path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404



@CheckValidUser
def ClassRegistration(request, id):
    classes = Class.objects.all()
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = forms.ClassRegistrationForm()
        selected_classes = request.POST.getlist('selection')
        for i in selected_classes:
            student.class_id.add(i)
        return HttpResponseRedirect(reverse('edit-class-registration-page', args=[id]))
    else:
        form = forms.ClassRegistrationForm()
    context = {'form': form, 'classes': classes, 'student': student}
    return render(request, 'User/class-registration.html', context)


@CheckValidUser
def EditClassRegistration(request, id):
    selected_classes = Class.objects.all()
    deadline = datetime(2021, 12, 31, 19, 59, 00)
    now = datetime.now()
    student = Student.objects.get(id=id)
    context = {'selected_classes': selected_classes, 'deadline': deadline, 'now': now, 'student': student}
    return render(request, 'User/edit-class-registration.html', context)


@CheckValidUser
def StaffContact(request, id, class_id):
    lecturer = Class.objects.get(id=class_id).lecturer.user_id
    return render(request, 'User/user-about.html', {"userObj": lecturer, "page_title": "Staff Contact"})


@CheckValidUser
def ViewStudentList(request, id, class_id):
    lecturer_class = Class.objects.get(id=class_id)
    '''
        for i in lecturer_class.student.values_list:
        student_list.append(i)
    '''
    student_list = lecturer_class.student_set.all()
    return render(request, 'Courses/class-student-list.html', {"student_list": student_list, "lecturer_class": lecturer_class})



