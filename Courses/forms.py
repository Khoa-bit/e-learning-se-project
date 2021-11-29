import pytz

from Courses.models import ClassAnnouncement, ClassContent, Class
from django import forms
import datetime

utc = pytz.UTC

class UploadClassAnnouncementForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'placeholder': 'Announcement Title'}))
    content = forms.CharField(label='Content', widget=forms.Textarea(
        attrs={'placeholder': 'Announcement Content'}))
    class Meta:
        model = ClassAnnouncement
        fields = [
            'title',
            'content'
        ]


class UploadClassContentForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'placeholder': 'Content Title'}))
    content = forms.CharField(label='Description', widget=forms.Textarea(
        attrs={'placeholder': 'Content Description'}))
    class Meta:
        model = ClassContent
        fields = [
            'attached_file',
            'title',
            'content',
        ]


class ClassRegistrationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices')
        super(ClassRegistrationForm,self).__init__(*args, **kwargs)
        self.fields['selection'] = forms.MultipleChoiceField(choices=choices,widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Class


class EditClassRegistrationForm(forms.Form):
    selection = forms.BooleanField(widget=forms.CheckboxSelectMultiple)


class EditClassAnnouncementForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'placeholder': 'Announcement Title'}))
    content = forms.CharField(label='Content', widget=forms.Textarea(attrs={'placeholder': 'Announcement Content'}))

    class Meta:
        model = ClassAnnouncement
        fields = ['title', 'content']


class EditClassContentForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'placeholder': 'Content Title'}))
    content = forms.CharField(label='Description', widget=forms.Textarea(attrs={'placeholder': 'Content Description'}))
    attached_file = forms.FileField(label='File', required=False, widget=forms.ClearableFileInput(attrs={'multiple':True}))
    class Meta:
        model = ClassContent
        fields = ['attached_file', 'title', 'content']