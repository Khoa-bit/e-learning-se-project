from django.urls import path
from . import views

urlpatterns = [
    path("view/", views.ClassworkView, name='classwork-view'),
    path("create/",views.CreateClassworkView, name='create-classwork-view'),
    path("<int:test_id>/edit/",views.EditClassworkView, name='edit-classwork-view'),
    path("<int:test_id>/do",views.DoTestView,name='do-test'),
    path("writtenform/",views.written_question_form,name='written-form'),
    path("multiplechoiceform/",views.multiplechoice_form,name='multiplechoice-form'),
    path("mcoform/",views.mco_form,name='mco-form'),
]
