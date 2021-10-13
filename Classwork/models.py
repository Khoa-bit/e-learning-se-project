from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Test(models.Model):
  class_id = models.ForeignKey("Course.Class",on_delete=CASCADE)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()

class Question(models.Model):
  test_id = models.ManyToManyField(Test)
  is_written = models.BooleanField()  # true if written question, false if multiplechoice
  question = models.TextField()
  solution = models.CharField(max_length=200,null=True,blank=True)

class MultipleChoiceOption(models.Model):
  Question = models.ForeignKey(Question,on_delete=CASCADE)
  Option = models.CharField(max_length=50)

class StudentAnswer(models.Model):
  student = models.ForeignKey('User.student',on_delete=CASCADE)
  question = models.ForeignKey(Question,on_delete=CASCADE)
  written_ans = models.TextField(blank=True,null=True)
  choice_ans = models.ForeignKey(MultipleChoiceOption,blank=True,null=True)



