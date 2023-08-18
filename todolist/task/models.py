from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=50)


class Tarefa(models.Model):
    titulo = models.CharField(verbose_name="título", max_length=250)
    descricao = models.TextField(verbose_name="descrição")
    data = models.DateField()
    estado = models.BooleanField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

