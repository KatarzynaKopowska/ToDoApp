from django.db import models
from django.utils import timezone

# Create your models here.


class Task(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(blank=True, null=True)
    is_finished = models.BooleanField()

    def __str__(self):
        return self.author


# class Subtask(models.Model):
#     name = models.CharField(max_length=200)
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
#     is_finished = models.BooleanField()
#
#     def __str__(self):
#         return self.name
