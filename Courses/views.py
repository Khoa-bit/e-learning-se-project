import os

import pytz
import datetime
import calendar
from calendar import HTMLCalendar

from django.forms import model_to_dict
from django.shortcuts import render
from django.utils import timezone
from django.http.response import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe

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
    student = Student.objects.get(id=id)
    student_class = Class.objects.get(id=class_id)
    ongoing,upcoming,overdue = [],[],[]
    # add filter here (check if test is in the time window because students can only see those tests)
    now = timezone.localtime()+timezone.timedelta(hours=7)
    for t in student_class.test_set.order_by('-time_modified'):
        is_new = None
        # is_new = timezone.now() - t.time_modified < timezone.timedelta(weeks=1)
        print("Hello?")
        if t.publish_time <= now and t.end_time >= now - t.available_time_after_deadline:
            print("added "+t.test_name+" to tests")
            ongoing.append({'obj': t, 'is_new': is_new})
        elif t.publish_time >= now:
            print("added "+t.test_name+" to upcoming")
            upcoming.append({'obj': t, 'is_new': is_new})
        elif t.end_time <= now - t.available_time_after_deadline and not t.studenttest_set.filter(student_id=student).exists():
            overdue.append({'obj': t, 'is_new': is_new})
        # else:
        #     overdue.append({'obj': t, 'is_new': is_new})
    content = {'student_class': student_class,'ongoing':ongoing,'upcoming':upcoming,'overdue':overdue} # tests that can be taken are in the test list and upcoming test are in the upcoming list
    return render(request, "Courses/class-assignment.html", content)


def fetch_class_assignments(lecturer_class):
    class_assignments = []
    for class_assignment in lecturer_class.test_set.order_by('-time_modified'):
        is_new = timezone.now() - class_assignment.time_modified < timezone.timedelta(weeks=1)
        class_assignments.append({"obj": class_assignment, "is_new": is_new})
    return class_assignments

@CheckValidUser
def LecturerClassAssignment(request, id, class_id):
    user = Lecturer.objects.get(id=id)
    if (class_id not in user.class_set.all().values_list('id', flat=True)):
        return HttpResponseRedirect(reverse("lecturer-announcement-page", args=[id]))
    lecturer_class = Class.objects.get(id=class_id)
    tests = fetch_class_assignments(lecturer_class)   # lecturers can see all tests
    content = {'lecturer_class': lecturer_class, 'ongoing':tests}
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
    file_path = str(settings.BASE_DIR).replace("\\","/") + path
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
    student_classes = student.class_id.all()
    choices = []
    for i in Class.objects.all():
        now = pytz.UTC.localize(datetime.now())
        if (i.start_date > now):
            choices.append((int(i.id), i.course.name))
    if request.method == 'POST':
        form = forms.ClassRegistrationForm(choices=choices)
        selected_classes = request.POST.getlist('selection')
        if not selected_classes:
            return HttpResponseRedirect(reverse('student-class-registration-page', args=[id]))
        else:
            for i in selected_classes:
                if int(i) in student.class_id.all().values_list('id',flat=True):
                    return HttpResponseRedirect(reverse('student-class-registration-page', args=[id]))
                else:
                    student.class_id.add(Class.objects.get(id=i))
            return HttpResponseRedirect(reverse('edit-class-registration-page', args=[id]))
    else:
        form = forms.ClassRegistrationForm(choices=choices)
    context = {'form': form, 'classes': classes, 'student': student, 'student_classes': student_classes}
    return render(request, 'User/class-registration.html', context)


@CheckValidUser
def EditClassRegistration(request, id):
    utc = pytz.UTC
    student = Student.objects.get(id=id)
    classes = []
    now = utc.localize(datetime.now())
    deadline = datetime(2021, 12, 31, 19, 59, 00)
    for i in student.class_id.all():
        if (i.start_date > now):
            classes.append(i)
    if request.method == 'POST':
        form = forms.EditClassRegistrationForm()
        selected_classes = request.POST.getlist('selection')
        print(selected_classes)
        if not selected_classes:
            for i in student.class_id.all():
                if i in classes:
                    student.class_id.remove(i)
            return HttpResponseRedirect(reverse('edit-class-registration-page', args=[id]))
        else:
            for i in student.class_id.all():
                if str(i.id) not in selected_classes:
                    student.class_id.remove(i)
            return HttpResponseRedirect(reverse('edit-class-registration-page', args=[id]))
    else:
        form = forms.EditClassRegistrationForm()
    is_past_deadline = False
    if now < deadline:
        is_past_deadline = True
    context = {'classes': classes, 'deadline': deadline, 'is_past_deadline': is_past_deadline, 'student': student, 'form': form}
    return render(request, 'User/edit-class-registration.html', context)


@CheckValidUser
def EditClassAnnouncement(request, id, class_id, announcement_id):
    lecturer = Lecturer.objects.get(id=id)
    lecturer_class = Class.objects.get(id=class_id)
    announcement = ClassAnnouncement.objects.get(id=announcement_id)
    if "post_button" in request.POST:
        form = forms.EditClassAnnouncementForm(request.POST or None, instance=announcement)
        if form.is_valid():
            form.save()
            if not announcement.is_displayable:
                announcement.time_modified = announcement.time_created
            return HttpResponseRedirect(reverse('lecturer-class-announcement-page', args=[id, class_id]))
    elif "delete_button" in request.POST:
        announcement.delete()
        return HttpResponseRedirect(reverse('lecturer-class-announcement-page', args=[id, class_id]))
    else:
        form = forms.EditClassAnnouncementForm(request.POST or None, instance=announcement)
    context = {"lecturer": lecturer, "announcement": announcement, "lecturer_class": lecturer_class, 'form': form}
    return render(request, 'User/edit-class-announcement.html', context)


@CheckValidUser
def EditClassContent(request, id, class_id, content_id):
    lecturer = Lecturer.objects.get(id=id)
    lecturer_class = Class.objects.get(id=class_id)
    content = ClassContent.objects.get(id=content_id)
    url = str(settings.BASE_DIR).replace("\\", "/") + "/media/"
    files = os.listdir(url)
    if "post_button" in request.POST:
        form = forms.EditClassContentForm(request.POST or None, request.FILES or None, instance=content)
        if form.is_valid():
            form.save()
            for i in files:
                if i not in ClassContent.objects.all().values_list('attached_file', flat=True):
                    remove_url = url + i
                    os.remove(remove_url)
        return HttpResponseRedirect(reverse('lecturer-class-content-page', args=[id, class_id]))
    elif "delete_button" in request.POST:
        content.delete()
        for i in files:
            if i not in ClassContent.objects.all().values_list('attached_file', flat=True):
                remove_url = url + i
                os.remove(remove_url)
        return HttpResponseRedirect(reverse('lecturer-class-content-page', args=[id, class_id]))
    else:
        form = forms.EditClassContentForm(request.POST or None, request.FILES or None, instance=content)
    context = {'lecturer': lecturer, 'lecturer_class': lecturer_class, 'post': content, 'form': form}
    return render(request, 'User/edit-class-content.html', context)


@CheckValidUser
def StudentClassFeedback(request, id, class_id):
    student = Student.objects.get(id=id)
    student_class = Class.objects.get(id=class_id)
    if "send_button" in request.POST:
        form = forms.UploadClassFeedbackForm(request.POST or None)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.class_id_id = class_id
            feedback.save()
            return HttpResponseRedirect(reverse('student-class-announcement-page', args=[id, class_id]))
    else:
        form = forms.UploadClassFeedbackForm(request.POST or None)
    context = {'student': student, 'student_class': student_class, 'form': form}
    return render(request, 'User/upload-feedback.html', context)


@CheckValidUser
def LecturerClassFeedback(request, id, class_id):
    lecturer = Lecturer.objects.get(id=id)
    lecturer_class = Class.objects.get(id=class_id)
    posts = lecturer_class.classfeedback_set.all()
    context = {'lecturer': lecturer, 'lecturer_class': lecturer_class, 'posts': posts.order_by('-time_created')}
    return render(request, 'User/view-feedback.html', context)



@CheckValidUser
def StaffContact(request, id, class_id):
    lecturer = Class.objects.get(id=class_id).lecturer.user_id
    return render(request, 'User/user-about.html', {"userObj": lecturer, "page_title": "Staff Contact"})


@CheckValidUser
def ViewStudentList(request, id, class_id):
    lecturer = Lecturer.objects.get(id=id)
    lecturer_class = Class.objects.get(id=class_id)
    student_list = lecturer_class.student_set.all().order_by('user_id__first_name')
    return render(request, 'Courses/class-student-list.html', {"student_list": student_list, "lecturer_class": lecturer_class, "lecturer": lecturer})


@CheckValidUser
def ViewStudentCoursePerformance(request, id, class_id, student_id):
    lecturer_class = Class.objects.get(id=class_id)
    student = Student.objects.get(id=student_id)
    tests = StudentTest.objects.filter(student_id=student)
    return render(request, 'Courses/view-student-course-performance.html', {"student": student,"tests":tests, "lecturer_class": lecturer_class})


@CheckValidUser
def ViewSelfCoursePerformance(request, id, class_id):
    student_class = Class.objects.get(id=class_id)
    student = Student.objects.get(id=id)
    tests = StudentTest.objects.filter(student_id=student.id)
    return render(request, 'Courses/view-student-course-performance.html', {"student": student, "tests":tests, 'student_class': student_class})