from django.shortcuts import render
from User.views import CheckValidUser
from django.http import HttpResponseRedirect
from django.urls import reverse
from Courses.models import Class
from User.models import Lecturer, Student, User
from .models import *
from .forms import *
# Create your views here.


def CreateClassworkView(request, id, class_id):
  context={'id':id,'class_id':class_id}
  if not request.user.is_lecturer():
    return HttpResponseRedirect(reverse("student-class-announcement-page"))
  if request.method == 'POST':
    print(request.POST)
  return render(request, "Classwork/create-classwork.html",context)

def ClassworkView(request, id, class_id):
  lecturer = Lecturer.objects.get(id=id)
  class_id = Class.objects.get(id=class_id)
  context={}
  tests = class_id.test_set.all()
  context['tests']=tests
  return render(request,'Classwork/view-classwork.html', context)

def EditClassworkView(request, id, class_id , test_id):
  # when the edit button is implemented
  lecturer = Lecturer.objects.get(id=id)
  class_id = Class.objects.get(id=class_id)
  test = Test.objects.get(id=test_id)

  context = {"test":test}
  return render(request,'Classwork/edit-classwork.html',context)

def DoTestView(request,id,class_id,test_id):
  if request.method == 'POST':
    print(request.POST)
  # student = User.objects.get(id=id).student
  class_id = Class.objects.get(id=test_id)
  test = Test.objects.get(id=test_id)
  context={'test':test,}
  return render(request,"Classwork/do-test.html",context)

def written_question_form(request,id,class_id):
  context={'form':WrittenQuestionForm()}
  return render(request,"Classwork/partials/partial-written-form.html",context)

def multiplechoice_form(request,id,class_id):
  context = {'form':MultipleChoiceQuestionForm(),"id":id,"class_id":class_id}
  return render(request,"Classwork/partials/partial-multiplechoice-form.html",context)

def mco_form(request,id,class_id):
  context = {'form': MultipleChoiceOptionForm(),"id":id,"class_id":class_id}
  return render(request,"Classwork/partials/partial-mco-form.html",context)