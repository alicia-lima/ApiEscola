from django.test import TestCase
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunosSerializer, CursoSerializer, MatriculaSerializer

class AlunoSerializerTestCase(TestCase):
    def setUp(self):
        self.aluno_1 = Aluno(
            id= 1, nome='Ana Carla', email='aninha@gmail.com', rg='418212594', 
            cpf='42334461024', celular='87 99654-3945', data_nascimento='1996-12-05',
        )

        self.serializer = AlunosSerializer(instance=self.aluno_1)
    
    def teste_verifica_campos_serializados_aluno(self):
        ''' Teste que verifica os campos dos alunos que estão sendo serializados 
            criando uma variável (data) que salva todas as informações do aluno criado no setUp
            e checa com o assertEqual atráves do set se todos campos foram preenchidos foram 
            preenchidos com alguma informação.
        '''

        data = self.serializer.data 
        self.assertEqual(set(data.keys()), set(['id', 'nome', 'email', 'rg', 'cpf', 'celular', 'data_nascimento', 'ativo', 'foto']))

    def teste_verifica_conteudo_dos_campos_serializados_alunos(self):
        ''' Teste que verifica o conteudo dos campos serializados '''
        
        data = self.serializer.data
        self.assertEqual(data['id'], self.aluno_1.id)
        self.assertEqual(data['nome'], self.aluno_1.nome)
        self.assertEqual(data['email'], self.aluno_1.email)
        self.assertEqual(data['rg'], self.aluno_1.rg)
        self.assertEqual(data['cpf'], self.aluno_1.cpf)
        self.assertEqual(data['celular'], self.aluno_1.celular)
        self.assertEqual(data['data_nascimento'], self.aluno_1.data_nascimento)

class CursoSeriazlizerTestCase(TestCase):
    def setUp(self):
        self.curso_1 = Curso(
            code_curso='CTT1', descricao='curso teste 1', nivel='B'
        )
        self.serializer = CursoSerializer(instance=self.curso_1)

    
    def teste_verifica_campos_serializados_curso(self):
        ''' Teste que verifica os campos dos cursos que estão sendo serializados 
            criando uma variável (data) que salva todas as informações do aluno criado no setUp
            e checa com o assertEqual atráves do set se todos campos foram preenchidos foram 
            preenchidos com alguma informação.
        '''
        data = self.serializer.data 
        self.assertEqual(set(data.keys()), set(['id','code_curso', 'descricao', 'nivel']))

    def teste_verifica_conteudo_dos_campos_serializados_cursos(self):
        ''' Teste que verifica o conteudo dos campos serializados '''
        
        data = self.serializer.data
        self.assertEqual(data['id'], self.curso_1.id)
        self.assertEqual(data['code_curso'], self.curso_1.code_curso)
        self.assertEqual(data['descricao'], self.curso_1.descricao)
        self.assertEqual(data['nivel'], self.curso_1.nivel)