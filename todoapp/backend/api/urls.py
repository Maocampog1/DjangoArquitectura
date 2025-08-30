from django.urls import path
from .views import ToDoListCreate

urlpatterns = [
    path('todos/', ToDoListCreate.as_view(), name='todo_list'),
]
