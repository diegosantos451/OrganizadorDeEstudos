
from django.db import models
from django.conf import settings


class Tarefa(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tarefas'
    )

    titulo = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    data_conclusao = models.DateField(null=True, blank=True)
    concluida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['concluida', 'data_conclusao']

    def __str__(self):
        return self.titulo
