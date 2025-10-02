from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
import re

def validar_cpf(value):
    # validação simples de formato (apenas dígitos; aqui não implementamos algoritmo do CPF)
    if not re.fullmatch(r"\d{11}", value):
        raise ValidationError("CPF deve ter 11 dígitos numéricos (ex: 12345678901).")

class Aluno(models.Model):
    nome = models.CharField("Nome", max_length=120)
    responsavel = models.CharField("Responsável", max_length=120, blank=True)
    email = models.EmailField("E-mail", unique=True)
    dt_nascimento = models.DateField("Data de nascimento")
    cpf = models.CharField("CPF", max_length=11, unique=True, validators=[validar_cpf])

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("escola:listar_aluno")

class Turma(models.Model):
    nome = models.CharField("Nome da Turma", max_length=120)
    carga_horaria = models.PositiveIntegerField("Carga Horária (h)")
    conteudo = models.TextField("Conteúdo")

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("escola:listar_turma")

class TurmaAluno(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name="vinculos")
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name="matriculas")

    class Meta:
        unique_together = ("aluno", "turma")
        ordering = ["turma", "aluno"]

    def __str__(self):
        return f"{self.aluno.nome} → {self.turma.nome}"

    def get_absolute_url(self):
        return reverse("escola:listar_turma_aluno")
