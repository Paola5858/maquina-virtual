from django.urls import path
from . import views

app_name = "escola"

urlpatterns = [
    # raiz -> lista de alunos
    path("", views.AlunoListView.as_view(), name="home"),

    # Alunos
    path("alunos/", views.AlunoListView.as_view(), name="listar_aluno"),
    path("alunos/novo/", views.AlunoCreateView.as_view(), name="novo_aluno"),
    path("alunos/editar/<int:pk>/", views.AlunoUpdateView.as_view(), name="editar_aluno"),
    path("alunos/excluir/<int:pk>/", views.AlunoDeleteView.as_view(), name="excluir_aluno"),

    # Turmas
    path("turmas/", views.TurmaListView.as_view(), name="listar_turma"),
    path("turmas/novo/", views.TurmaCreateView.as_view(), name="nova_turma"),
    path("turmas/editar/<int:pk>/", views.TurmaUpdateView.as_view(), name="editar_turma"),
    path("turmas/excluir/<int:pk>/", views.TurmaDeleteView.as_view(), name="excluir_turma"),

    # TurmaAluno (vínculo)
    path("turma-aluno/", views.TurmaAlunoListView.as_view(), name="listar_turma_aluno"),
    path("turma-aluno/novo/", views.TurmaAlunoCreateView.as_view(), name="novo_turma_aluno"),
    path("turma-aluno/editar/<int:pk>/", views.TurmaAlunoUpdateView.as_view(), name="editar_turma_aluno"),
    path("turma-aluno/excluir/<int:pk>/", views.TurmaAlunoDeleteView.as_view(), name="excluir_turma_aluno"),
]
