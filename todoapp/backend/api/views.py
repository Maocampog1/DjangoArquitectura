from rest_framework import generics, permissions
from .serializers import ToDoSerializer, ToDoToggleCompleteSerializer
from todo.models import ToDo
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods

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


# -------- Signup & Login (Token) --------

@csrf_exempt
@require_http_methods(["POST"])
def signup(request):
    try:
        data = JSONParser().parse(request)  # dict con 'username' y 'password'
        user = User.objects.create_user(
            username=data['username'],
            password=data['password']
        )
        user.save()
        token = Token.objects.create(user=user)
        return JsonResponse({'token': str(token)}, status=201)
    except IntegrityError:
        return JsonResponse({'error': 'username ya existe, elige otro'}, status=400)
    except KeyError:
        return JsonResponse({'error': 'faltan campos: username y password'}, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def login(request):
    data = JSONParser().parse(request)
    user = authenticate(
        request,
        username=data.get('username'),
        password=data.get('password')
    )
    if user is None:
        return JsonResponse({'error': 'no se pudo iniciar sesión: revisa usuario/clave'}, status=400)

    # devolver token (crearlo si no existe)
    token, _ = Token.objects.get_or_create(user=user)
    return JsonResponse({'token': str(token)}, status=201)