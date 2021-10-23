from uuid import uuid4
from django.http.response import HttpResponse
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
  if request.method == 'POST':
    form = TestForm(data=request.POST)
    if(form.is_valid()):
      t = form.save(commit=False)
      t.class_id = Class.objects.get(id=class_id)
      t.save()
      return HttpResponseRedirect(reverse("classwork-view",args=[id,class_id]))
  else:
    form = TestForm()
  context['form'] = form
  return render(request, "Classwork/create-classwork.html",context)

def ClassworkView(request, id, class_id):
  lecturer = Lecturer.objects.get(id=id)
  c = Class.objects.get(id=class_id)
  context={'id':id,'class_id':class_id}
  tests = c.test_set.all()
  context['tests']=tests
  return render(request,'Classwork/view-classwork.html', context)

def EditClassworkView(request, id, class_id , test_id):
  # when the edit button is implemented
  lecturer = Lecturer.objects.get(id=id)
  class_id = Class.objects.get(id=class_id)
  test = Test.objects.get(id=test_id)
  if request.method == "POST":
    print(request.POST)
  context = {'id':id,'class_id':class_id.id,'test':test,'test_id':test_id}
  return render(request,'Classwork/edit-classwork.html',context)

def DoTestView(request,id,class_id,test_id):
  if request.method == 'POST':
    print(request.POST)
  # student = User.objects.get(id=id).student
  class_id = Class.objects.get(id=test_id)
  test = Test.objects.get(id=test_id)
  context={'test':test,}
  return render(request,"Classwork/do-test.html",context)

def written_question_form(request,id,class_id,test_id):
  form = MultipleChoiceQuestionForm()
  if request.method == 'POST':
    q = Question(question=request.POST['question'],is_written=True,test_id=Test.objects.get(id=test_id))
    q.save()
    return HttpResponseRedirect(reverse("edit-classwork-view",args=[id,class_id,test_id]))
  context={'form':form}
  return render(request,"Classwork/partials/partial-written-form.html",context)

def multiplechoice_form(request,id,class_id,test_id):
  error=""
  form = MultipleChoiceQuestionForm()
  qid=str(uuid4())[:5]
  form.fields['q.'+qid]=form.fields['question']
  del form.fields['question']
  context = {'form':form,"id":id,"class_id":class_id,"qid":qid}
  if request.method == 'POST':
    questions,options,correctoptions = parseMultipleChoice(request)
    for k,v in questions.items():
      q = Question(question=v,is_written=False,test_id=Test.objects.get(id=test_id))
      q.save()
      for m,n in options.items():
        if m in correctoptions.keys():
          o = MultipleChoiceOption(option=n,is_true=True,question=q)
        else:
          o=MultipleChoiceOption(option=n,is_true=False,question=q)
        o.save()
    return HttpResponseRedirect(reverse("edit-classwork-view",args=[id,class_id,test_id]))
  return render(request,"Classwork/partials/partial-multiplechoice-form.html",context)

def parseMultipleChoice(request):
  questions={}
  options={}
  correctoptions={}
  for i in request.POST.keys():
    if 'q.' in i:
      questions[i]=request.POST[i]
    if 'o.' in i:
      options={request.POST.getlist('optionid')[k]:request.POST.getlist(i)[k] for k in range(len(request.POST.getlist(i)))}
  for k,v in options.items():
    if "i."+k in request.POST.keys():
      correctoptions[k]=v
  return (questions,options,correctoptions)

def mco_form(request,id,class_id,qid):
  oid = str(uuid4())[:5]
  form = MultipleChoiceOptionForm(initial={'optionid':oid})
  form.fields['o.'+qid]=form.fields['option']
  del form.fields['option']
  form.fields['i.'+oid]=form.fields['is_true']
  del form.fields['is_true']
  context = {'form': form,"id":id,"class_id":class_id}
  return render(request,"Classwork/partials/partial-mco-form.html",context)

def DeleteTest(request,id,class_id,test_id):
  test = Test.objects.get(id=test_id)
  context = {'id':id,'class_id':class_id,'test_id':test_id,'test':test}
  if request.method == "POST":
    test.delete()
    return HttpResponseRedirect(reverse("classwork-view",args=[id,class_id]))
  return render(request,"Classwork/delete-classwork.html",context)

def DeleteQuestion(request,id,class_id,test_id,qid):
  q = Question.objects.get(id=qid)
  q.delete()
  return HttpResponseRedirect(reverse("edit-classwork-view",args=[id,class_id,test_id]))

def UpdateQuestion(request,id,class_id,test_id,qid):
  q=Question.objects.get(id=qid)
  context={'id':id,'class_id':class_id,'test_id':test_id,'question':q}
  if request.method == "POST":
    if q.is_written:
      for option in q.multiplechoiceoption_set.all():
        option.option = request.POST.getlist(str(option.id))[0]
        if len(request.POST.getlist(str(option.id))) == 2:
          option.is_true=True
        else:
          option.is_true=False
        option.save()
    return HttpResponseRedirect(reverse("edit-classwork-view",args=[id,class_id,test_id]))
  return render(request,"Classwork/update-question.html",context)