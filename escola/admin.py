from django.contrib import admin
from .models import Aluno, Turma, TurmaAluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cpf', 'dt_nascimento')
    search_fields = ('nome', 'email', 'cpf')

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'carga_horaria', 'conteudo')
    search_fields = ('nome',)

@admin.register(TurmaAluno)
class TurmaAlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'turma')
    search_fields = ('aluno__nome', 'turma__nome')
