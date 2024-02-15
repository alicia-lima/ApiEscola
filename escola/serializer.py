from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula
from escola.validators import cpf_valido, nome_valido, rg_valido, celular_valido

class AlunosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

    def validate(self, data):
        
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'Número de CPF inválido'})
    
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'O nome não pode conter número ou símbolos'})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'O CPF deve ter 9 digitos'})
        
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':'o número deve seguir este modelo: 11 91234-1234'})
        return data

class AlunosSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento', 'ativo']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso 
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculaAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']
    