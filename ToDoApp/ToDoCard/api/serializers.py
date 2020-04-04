from rest_framework import serializers
from ToDoCard.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'author', 'title', 'description', 'created_date', 'is_finished', 'name']

