from django.urls import path
from .views import *

urlpatterns = [
    path("test/", CreateQuizView,name='create-quiz'),
]
