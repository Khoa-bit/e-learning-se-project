
from django.db.models.deletion import CASCADE
from django.db import models
from django.utils import timezone
# Create your models here.

class Announcement(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField(max_length=1000)
  time_created = models.DateTimeField()

  def __str__(self):
    return self.title
