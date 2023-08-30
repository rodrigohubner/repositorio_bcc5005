from rest_framework import viewsets
from .models import Usuario, Tarefa
from .serializers import UsuarioSerializer, TarefaSerializer


class TarefaViewSet(viewsets.ModelViewSet):
    serializer_class = TarefaSerializer
    queryset = Tarefa.objects.all()


class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()