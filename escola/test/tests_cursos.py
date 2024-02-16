from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status


class CursosTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            code_curso='CTT1', descricao='curso teste 1', nivel='B'
        )
        self.curso_2 = Curso.objects.create(
            code_curso='CTT2', descricao='curso teste 2', nivel='I'
        )

    # def test_falhador(self):
    #     self.fail('Teste falhou de proposito, não se preocupe')
    
    def test_requisicao_get_para_listar_cursos(self):
        ''' Teste para verificar se a requisição GET para listar os cursos 
            criando uma variável (response) que recebe uma solicitação (get)
            de um cliente e compara (assertEqual) com o status 200
        
        '''
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_cursos(self):
        ''' Teste para verificar se a requisição POST para criar um curso 
            criando uma variável (data) que recebe a informação necessária 
            para criar o curso de acordo com models (Curso) depois outra váriavel (response)
            que recebe uma solicitação (post) de um cliente e compara (assertEqual) com o status 201
        
        '''
        data = {
            'code_curso': 'CTT3',
            'descricao':'Curso teste 3',
            'nivel': 'A'
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_deletar_curso(self):
        ''' Teste para verificar a requisição DELETE não premitida para deletar um curso
            cria uma váriavel (response) que recebe uma solicitação (delete) de um cliente 
            e compara (assertEqual) com o status 405
        '''
        
        response = self.client.delete('/cursos/1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_requisicao_put_para_atualizar_curso(self):
        ''' Teste para verificar a requisição PUT para atualizar curso
            criando uma variável (data) que recebe a informação necessária para atualizar 
            o curso de acordo com models (Curso) depois outra váriavel (response) que recebe 
            uma solicitação (put) de um cliente e compara (assertEqual) com o status 200
        '''

        data = {
            'code_curso': 'CTT1',
            'descricao': 'curso teste 1 atualizado',
            'nivel': 'A'
        }

        response = self.client.put('/cursos/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)