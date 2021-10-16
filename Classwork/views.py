from django.shortcuts import render
from User.views import CheckValidUser
from django.http import HttpResponseRedirect
from django.urls import reverse
from Courses.models import Class
from User.models import Lecturer, Student
# Create your views here.


def CreateQuizView(request):
  
  context={}
  if not request.user.is_lecturer():
    return HttpResponseRedirect(reverse("guest-announcement-page"))
  return render(request, "Classwork/create-quiz.html",context)

def ClassworkView(request, id, class_id):
  lecturer = Lecturer.objects.get(id=id)
  class_id = Class.objects.get(id=class_id)
  context={}
  tests = class_id.test_set.all()
  context['tests']=tests
  return render(request,'Classwork/view-quiz.html', context)
