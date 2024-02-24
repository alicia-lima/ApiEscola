from rest_framework.test import APITestCase
from datetime import date
from escola.models import Aluno
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User


class AlunosTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Alunos-list')
        self.user = User.objects.create_user('c3po', password='123456')
        self.aluno_1 = Aluno.objects.create(
            id= '1', nome='Ana Carla', email='aninha@gmail.com', rg='418212594', 
            cpf='42334461024', celular='87 99654-3945', data_nascimento=date(1996,12,5),
        )
        self.aluno_2 = Aluno.objects.create(
            id= '2', nome='João Pedro', email='pedrinho@gmail.com', rg='160604618', 
            cpf='48132798058', celular='31 99202-0188', data_nascimento=date(2000,1,1),
        )
    
    def test_requisicao_get_para_listar_alunos(self):
        ''' Teste para verificar se a requisição GET para listar os alunos 
            criando uma variável (response) que recebe uma solicitação (get)
            de um cliente e compara (assertEqual) com o status 200
        
        '''
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_Aluno(self):
        ''' Teste para verificar se a requisição POST para criar um aluno 
            criando uma variável (data) que recebe a informação necessária 
            para criar o curso de acordo com models (Aluno) depois outra váriavel (response)
            que recebe uma solicitação (post) de um cliente e compara (assertEqual) com o status 201
        
        '''

        data = {
            'id': 3,
            'nome': 'Carla Alves',
            'email':'carlinha@gmail.com',
            'rg': '474150227',
            'cpf': '47255820000',
            'celular':'68 99452-4664',
            'data_nascimento': '2001-02-04',
            'ativo': True
        }

        self.client.force_authenticate(self.user)
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_deletar_aluno(self):
        ''' Teste para verificar a requisição DELETE para deletar um aluno
            cria uma váriavel (response) que recebe uma solicitação (delete) de um cliente 
            e compara (assertEqual) com o status 200
        '''
        
        self.client.force_authenticate(self.user)
        response = self.client.delete('/alunos/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_curso(self):
        ''' Teste para verificar a requisição PUT para atualizar um aluno
            criando uma variável (data) que recebe a informação necessária para atualizar 
            o curso de acordo com models (Aluno) depois outra váriavel (response) que recebe 
            uma solicitação (put) de um cliente e compara (assertEqual) com o status 200
        '''
        
        data = {
            'id': 1,
            'nome': 'Ana Carla',
            'email':'aninha@gmail.com',
            'rg': '418212594',
            'cpf': '42334461024',
            'celular':'87 99654-3945',
            'data_nascimento': '1995-03-05'
        }

        self.client.force_authenticate(self.user)
        response = self.client.put('/alunos/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)