from django import forms
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
