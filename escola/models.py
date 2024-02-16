from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    email = models.EmailField(blank=False, max_length=30, default='')
    rg = models.CharField(max_length=9, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    celular = models.CharField(max_length=14, null=False, blank=False, default='')
    data_nascimento = models.DateField()
    ativo = models.BooleanField(default=False)
    foto = models.ImageField(blank=True)

    def __str__ (self):
        return self.nome   

class Curso(models.Model):

    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )

    code_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False,default='B')

    def __str__ (self):
        return self.descricao   

class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno')
    )

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False,default='M')
     
''' 
    models.Foreignkey() = é utilizado no Django para criar um relacionamento de 
    chave estrangeira entre duas tabelas em um banco de dados.
    
    on_delete=models.CASCADE = indica que, caso um aluno ou curso seja deletado, 
    as matrículas relacionadas a ele também devem ser deletadas.
'''