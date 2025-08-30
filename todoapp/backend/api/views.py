from rest_framework import generics, permissions
from .serializers import ToDoSerializer
from todo.models import ToDo

class ToDoListCreate(generics.ListCreateAPIView):
    """
    GET  /api/todos/  -> lista los ToDos del usuario autenticado
    POST /api/todos/  -> crea un ToDo para el usuario autenticado
    """
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]  # exige login

    def get_queryset(self):
        user = self.request.user
        return ToDo.objects.filter(user=user).order_by('-created')

    def perform_create(self, serializer):
        # Asigna el usuario autenticado al nuevo ToDo
        serializer.save(user=self.request.user)
