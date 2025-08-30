from rest_framework import serializers
from todo.models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()

    class Meta:
        model = ToDo
        fields = ['id', 'title', 'memo', 'created', 'completed']


class ToDoToggleCompleteSerializer(serializers.ModelSerializer):
    """
    Serializer para el endpoint de toggle. No recibe campos de entrada;
    solo devuelve el estado actualizado.
    """
    class Meta:
        model = ToDo
        fields = ['id', 'completed']
        read_only_fields = ['id', 'completed']
