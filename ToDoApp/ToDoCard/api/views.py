from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ToDoCard.models import Task
from .serializers import TaskSerializer


def home_page(request):
    return HttpResponse("Home page")


@api_view(["GET", ])
def api_detail_task_view(request):
    try:
        task_detail = Task.objects.all()
    except Task.DoesNotExists:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TaskSerializer(task_detail, many=True)
        return Response(serializer.data)

