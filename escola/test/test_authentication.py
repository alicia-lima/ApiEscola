from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate

class AuthhenticationUserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('c3po', password='123456')
    
    def test_atenticacao_user_com_credenciais_corretas(self):
        ''' Teste que verifica a autenticação de um User com as credenciais corretas '''

        user = authenticate(username='c3po', password='123456')
        self.assertTrue(user is not None and user.is_authenticated)


    def test_autenticacao_de_user_com_username_incorreto(self):
        ''' Teste que verifica se p user não consegue logar caso o username está incorreto'''
        user = authenticate(username='c3pp', password='123456')
        self.assertFalse(user is not None and user.is_authenticated)
    
    def test_autenticacao_de_user_com_password_incorreto(self):
        ''' Teste que verifica se p user não consegue logar caso o password está incorreto'''
        user = authenticate(username='c3po', password='123455')
        self.assertFalse(user is not None and user.is_authenticated)