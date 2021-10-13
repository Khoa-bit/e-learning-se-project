
from django.db.models.deletion import CASCADE
from django.db import models
# Create your models here.

class Announcement(models.Model):
  author_id = models.ForeignKey("User.Lecturer",on_delete=CASCADE)
  title = models.CharField(max_length=100, blank=True)
  content = models.TextField()
  time_announced = models.DateTimeField()
  #course=models.ForeignKey("Courses.Course",on_delete=CASCADE,null=True)
