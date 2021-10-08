from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # Đừng chuyển 2 cái path này qua User.urls nha
    # Vì mấy cái {% url _ arg1 arg2 %} mà cần 2 params thì PyCharm IDE tui nó báo lỗi, auto-complete ko đc :<
    path('student/<int:id>/class/<int:class_id>/announcement', views.StudentClassAnnouncement, name='student-class-announcement-page'),
    path('student/<int:id>/class/<int:class_id>/content', views.StudentClassContent, name='student-class-content-page'),
]