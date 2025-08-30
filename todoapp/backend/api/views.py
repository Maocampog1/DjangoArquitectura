from rest_framework import generics, permissions
from .serializers import ToDoSerializer
from todo.models import ToDo

class ToDoListCreate(generics.ListCreateAPIView):
    """
    GET  /api/todos/  -> lista los ToDos del usuario autenticado
    POST /api/todos/  -> crea un ToDo para el usuario autenticado
    """
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]  # <- clave

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user).order_by('-created')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
