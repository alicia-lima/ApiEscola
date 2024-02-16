from rest_framework import viewsets, generics, filters, status
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunosSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculaAlunoSerializer, ListaAlunosMatriculadosSerializer, AlunosSerializerV2
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class AlunosViewsSet (viewsets.ModelViewSet):
    ''' Exibindo todos os alunos e alunas  '''

    queryset = Aluno.objects.all()
    serializer_class = AlunosSerializer
    # filter_backends = [filter.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    filterset_fields = ['ativo']
    ''' Escolhendo a versão que irá ser chama '''
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return AlunosSerializerV2
        else: 
            return AlunosSerializer
  
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response 

class CursosViewSet (viewsets.ModelViewSet):
    ''' Exibindo todos os Cursos'''
    
    queryset = Curso.objects.all().order_by('code_curso')
    serializer_class = CursoSerializer
    http_method_names = ['get', 'post', 'put', 'path']

class MatriculaViewSet (viewsets.ModelViewSet):
    ''' Exibindo todas as Maticulas '''

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    http_method_names = ['get', 'post', 'put', 'path']
    
    @method_decorator(cache_page(100))
    def dispatch(self, request, *args, **kwargs):
        return super(MatriculaViewSet, self).dispatch(request, *args, **kwargs) 

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

