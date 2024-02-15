from rest_framework import viewsets, generics, filters
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunosSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculaAlunoSerializer, ListaAlunosMatriculadosSerializer, AlunosSerializerV2
from django_filters.rest_framework import DjangoFilterBackend


class AlunosViewsSet (viewsets.ModelViewSet):
    ''' Exibindo todos os alunos e alunas  '''

    queryset = Aluno.objects.all()
    serializer_class = AlunosSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    filterset_fields = ['ativo']
    ''' Escolhendo a versão que irá ser chama '''
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return AlunosSerializerV2
        else: 
            return AlunosSerializer

class CursosViewSet (viewsets.ModelViewSet):
    ''' Exibindo todos os Cursos'''
    
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet (viewsets.ModelViewSet):
    ''' Exibindo todas as Maticulas '''

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    http_method_names = ['get', 'post', 'put', 'path']

class ListaMatriculasAluno(generics.ListAPIView):
    ''' Listando as matriculas de um aluno(a) específico '''
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculaAlunoSerializer

class ListaAlunosMatriculados(generics.ListAPIView):
    ''' Listando alunos matriculados em um curso'''

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer

