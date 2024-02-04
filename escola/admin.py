from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

class Alunos(admin.ModelAdmin):
    list_display = ( 'id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    ordering = ('nome',)
    list_per_page = 10

admin.site.register(Aluno,Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'code_curso', 'descricao')
    list_display_links = ('id', 'code_curso')
    search_fields = ('code_curso',)

admin.site.register(Curso, Cursos)


class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'curso', 'periodo')
    list_display_links = ('id',)

admin.site.register(Matricula, Matriculas)