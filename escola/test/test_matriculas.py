from rest_framework.test import APITestCase
from escola.models import Matricula, Aluno, Curso
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
import json

class MatriculaTestCase(APITestCase):
    fixtures = ['matriculas']

    def setUp(self):
        self.list_url = reverse('Matricula-list')
        self.user = User.objects.create_user('c3po', password='123456')

    def test_verifica_carregamento_da_fixture(self):
        aluno = Aluno.objects.get(nome='Ana Carla')
        todos_os_alunos = Aluno.objects.all()
        self.assertEqual(aluno.nome, 'Ana Carla')
        self.assertEqual(len(todos_os_alunos), 2)

    # def test_criar_matricula(self):
    #     aluno = Aluno.objects.get(nome="Ana Carla")
    #     curso = Curso.objects.get(descricao="Curso teste 2")

    #     matricula = Matricula.objects.create(
    #         periodo='M',
    #         aluno=aluno,
    #         curso=curso
    #     )

    #     self.assertEqual(matricula.aluno, aluno)
    #     self.assertEqual(matricula.curso, curso)