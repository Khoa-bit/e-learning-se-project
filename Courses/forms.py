from django import forms
from Courses.models import ClassAnnouncement

class UploadClassAnnouncementForm(forms.ModelForm):
    class Meta:
        model = ClassAnnouncement
        fields = [
            'title',
            'content'
        ]