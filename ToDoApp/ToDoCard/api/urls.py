from django.urls import path
from .views import api_detail_task_view
from .views import home_page

app_name = 'ToDoCard'

urlpatterns = [
    path('', home_page),
    path('todo/', api_detail_task_view),
]
