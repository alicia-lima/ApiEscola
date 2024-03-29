
from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewsSet, CursosViewSet, MatriculaViewSet, ListaMatriculasAluno, ListaAlunosMatriculados
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter() #AJUDA A GERENCIAR ROTAS 

router.register('alunos', AlunosViewsSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matricula', MatriculaViewSet, basename='Matricula')


urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('controle-geral/', admin.site.urls),
    path('', include (router.urls) ),
    path('alunos/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
