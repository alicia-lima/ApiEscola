from rest_framework import viewsets, generics, filters
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunosSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculaAlunoSerializer, ListaAlunosMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


class AlunosViewsSet (viewsets.ModelViewSet):
    ''' Exibindo todos os alunos e alunas  '''

    queryset = Aluno.objects.all()
    serializer_class = AlunosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    filterset_fields = ['ativo']

class CursosViewSet (viewsets.ModelViewSet):
    ''' Exibindo todos os Cursos'''
    
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MatriculaViewSet (viewsets.ModelViewSet):
    ''' Exibindo todas as Maticulas '''

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaMatriculasAluno(generics.ListAPIView):
    ''' Listando as matriculas de um aluno(a) específico '''
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculaAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaAlunosMatriculados(generics.ListAPIView):
    ''' Listando alunos matriculados em um curso'''

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

