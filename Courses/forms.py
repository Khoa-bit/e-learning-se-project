from django import forms
from Courses.models import ClassAnnouncement, ClassContent

class UploadClassAnnouncementForm(forms.ModelForm):
    class Meta:
        model = ClassAnnouncement
        fields = [
            'title',
            'content'
        ]


class UploadClassContentForm(forms.ModelForm):
    class Meta:
        model = ClassContent
        fields = [
            'title',
            'content',
            'attached_file'
        ]