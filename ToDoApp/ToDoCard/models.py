from django.db import models
from django.utils import timezone

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    is_finished = models.BooleanField()

