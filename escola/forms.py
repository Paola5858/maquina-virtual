from django import forms
from django.core.exceptions import ValidationError
import re
from .models import Aluno, Turma, TurmaAluno

class BaseModelForm(forms.ModelForm):
    """Form base para adicionar Bootstrap 5 automaticamente."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            css = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = (css + " form-control").strip()
            if not field.widget.attrs.get("placeholder"):
                field.widget.attrs["placeholder"] = field.label

class AlunoForm(BaseModelForm):
    def clean_nome(self):
        nome = self.cleaned_data.get('nome', '').strip()
        if nome:
            # Formatação automática: título case
            nome = nome.title()
        return nome

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf', '').strip()
        if cpf:
            # Remove caracteres não numéricos
            cpf = re.sub(r'\D', '', cpf)
            # Valida formato
            if not re.fullmatch(r'\d{11}', cpf):
                raise ValidationError("CPF deve ter 11 dígitos numéricos.")
            # Valida algoritmo (simplificado, já validado no model)
            if cpf == cpf[0] * 11:
                raise ValidationError("CPF inválido.")
        return cpf

    def clean(self):
        cleaned_data = super().clean()
        dt_nascimento = cleaned_data.get('dt_nascimento')
        responsavel = cleaned_data.get('responsavel')

        # Validação cross-field: se menor de idade, responsável obrigatório
        if dt_nascimento:
            from datetime import date
            idade = (date.today() - dt_nascimento).days // 365
            if idade < 18 and not responsavel:
                raise ValidationError("Responsável é obrigatório para menores de 18 anos.")

        return cleaned_data

    class Meta:
        model = Aluno
        fields = ["nome", "responsavel", "email", "dt_nascimento", "cpf"]
        widgets = {
            "dt_nascimento": forms.DateInput(attrs={"type": "date"}),
            "cpf": forms.TextInput(attrs={"pattern": r"\d{11}", "title": "11 dígitos numéricos"}),
        }

class TurmaForm(BaseModelForm):
    class Meta:
        model = Turma
        fields = ["nome", "carga_horaria", "conteudo"]
        widgets = {
            "conteudo": forms.Textarea(attrs={"rows": 3}),
        }

class TurmaAlunoForm(forms.ModelForm):
    class Meta:
        model = TurmaAluno
        fields = ["aluno", "turma"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs["class"] = "form-select"
