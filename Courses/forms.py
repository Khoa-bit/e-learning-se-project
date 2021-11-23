from Courses.models import ClassAnnouncement, ClassContent, Class
from django import forms

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
    CLASS_CHOICES = []
    for i in Class.objects.all():
        CLASS_CHOICES.append((i.id, i))
    selection = forms.MultipleChoiceField(choices=CLASS_CHOICES, widget=forms.CheckboxSelectMultiple)





