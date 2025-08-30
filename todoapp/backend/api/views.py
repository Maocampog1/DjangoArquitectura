from rest_framework import generics, permissions
from .serializers import ToDoSerializer, ToDoToggleCompleteSerializer
from todo.models import ToDo


class ToDoListCreate(generics.ListCreateAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user).order_by('-created')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ToDoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user)


class ToDoToggleComplete(generics.UpdateAPIView):
    """
    PUT /api/todos/<id>/complete/  -> invierte (toggle) el campo completed
    """
    serializer_class = ToDoToggleCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Solo ToDos del usuario autenticado
        return ToDo.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        # Alterna completed y guarda
        instance = serializer.instance
        instance.completed = not instance.completed
        instance.save()
