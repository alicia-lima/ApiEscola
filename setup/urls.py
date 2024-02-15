
from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewsSet, CursosViewSet, MatriculaViewSet, ListaMatriculasAluno, ListaAlunosMatriculados
from rest_framework import routers

router = routers.DefaultRouter() #AJUDA A GERENCIAR ROTAS 

router.register('alunos', AlunosViewsSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matricula', MatriculaViewSet, basename='Matricula')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include (router.urls) ),
    path('alunos/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view()),
]
