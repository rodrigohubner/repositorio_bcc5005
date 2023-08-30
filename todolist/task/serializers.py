from .models import Tarefa, Usuario
from rest_framework import serializers


class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ["id", "titulo",
                  "descricao", "data",
                  "estado", "usuario"]

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome']