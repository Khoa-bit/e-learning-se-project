from django import forms
from django.forms import widgets
from .models import *



class TestForm(forms.ModelForm):
  class Meta:
    model = Test
    fields = ["test_name","test_description","publish_time","end_time","available_time_after_deadline"]
    widgets={
      "publish_time":widgets.DateTimeInput(attrs={'type':'datetime-local'}),
      "end_time":forms.DateTimeInput(attrs={'type':'datetime-local'}),
    }

class WrittenQuestionForm(forms.Form):
  question = forms.CharField()

class MultipleChoiceQuestionForm(forms.Form):
  question = forms.CharField()

class MultipleChoiceOptionForm(forms.Form):
  option = forms.CharField()
  is_true = forms.BooleanField(label = "Is true",required=False,initial=False)

# class WrittenQuestionForm(forms.ModelForm):
#   class Meta:
#     model = Question
#     fields = ["question"]

# class MultipleChoiceQuestionForm(forms.ModelForm):
#   class Meta:
#     model = Question
#     fields = ["question"]

# class MultipleChoiceOptionForm(forms.ModelForm):
#   class Meta:
#     model = MultipleChoiceOption
#     fields = ["is_true","option"]