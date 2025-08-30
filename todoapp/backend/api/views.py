from rest_framework import generics, permissions
from .serializers import ToDoSerializer
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
