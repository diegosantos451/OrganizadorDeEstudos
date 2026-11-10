
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Tarefa


class TarefaTests(TestCase):

    def setUp(self):
        self.usuario = User.objects.create_user(
            username='aluno',
            password='senha123'
        )
        self.client.login(
            username='aluno',
            password='senha123'
        )

    def test_criar_tarefa(self):
        resposta = self.client.post(
            reverse('criar_tarefa'),
            {
                'titulo': 'Estudar Python',
                'descricao': 'Revisar Django',
                'data_conclusao': '2026-11-15'
            }
        )

        self.assertEqual(resposta.status_code, 302)
        self.assertTrue(
            Tarefa.objects.filter(
                usuario=self.usuario,
                titulo='Estudar Python'
            ).exists()
        )

    def test_listar_tarefas(self):
        Tarefa.objects.create(
            usuario=self.usuario,
            titulo='Estudar Django'
        )

        resposta = self.client.get(reverse('lista_tarefas'))

        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'Estudar Django')

    def test_concluir_tarefa(self):
        tarefa = Tarefa.objects.create(
            usuario=self.usuario,
            titulo='Estudar Python'
        )

        self.client.post(
            reverse('concluir_tarefa', args=[tarefa.id])
        )

        tarefa.refresh_from_db()
        self.assertTrue(tarefa.concluida)

    def test_excluir_tarefa(self):
        tarefa = Tarefa.objects.create(
            usuario=self.usuario,
            titulo='Estudar HTML'
        )

        self.client.post(
            reverse('excluir_tarefa', args=[tarefa.id])
        )

        self.assertFalse(
            Tarefa.objects.filter(id=tarefa.id).exists()
        )

    def test_usuario_nao_pode_excluir_tarefa_de_outro(self):
        outro_usuario = User.objects.create_user(
            username='outro',
            password='senha123'
        )

        tarefa = Tarefa.objects.create(
            usuario=outro_usuario,
            titulo='Tarefa particular'
        )

        resposta = self.client.post(
            reverse('excluir_tarefa', args=[tarefa.id])
        )

        self.assertEqual(resposta.status_code, 404)
        self.assertTrue(
            Tarefa.objects.filter(id=tarefa.id).exists()
        )

    def test_usuario_nao_autenticado_nao_acessa_tarefas(self):
        self.client.logout()

        resposta = self.client.get(reverse('lista_tarefas'))

        self.assertEqual(resposta.status_code, 302)
