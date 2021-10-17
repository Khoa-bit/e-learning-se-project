from django import forms
from .models import *

class WrittenQuestionForm(forms.Form):
  question = forms.CharField()

class MultipleChoiceQuestionForm(forms.Form):
  question = forms.CharField()

class MultipleChoiceOptionForm(forms.Form):
  option = forms.CharField()
  is_true = forms.BooleanField(label = "Is true")