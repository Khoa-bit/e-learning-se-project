from Courses.models import ClassAnnouncement, ClassContent
from django import forms

class UploadClassAnnouncementForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'placeholder': 'Announcement Title'}))
    content = forms.CharField(label='Content', widget=forms.Textarea(attrs={'placeholder': 'Announcement Content', 'rows': 30, 'cols': 100}))
    class Meta:
        model = ClassAnnouncement
        fields = [
            'title',
            'content'
        ]


class UploadClassContentForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'placeholder': 'Content Title'}))
    content = forms.CharField(label='Description', widget=forms.Textarea(
        attrs={'placeholder': 'Content Description', 'rows': 30, 'cols': 30}))
    class Meta:
        model = ClassContent
        fields = [
            'title',
            'content',
            #'attached_file'
        ]