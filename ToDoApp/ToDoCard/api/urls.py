from django.urls import path
from .views import api_detail_task_view

app_name = 'ToDoCard'

urlpatterns = [
    path('todo/', api_detail_task_view),
]
