from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from .models import Aluno, Turma, TurmaAluno
from .forms import AlunoForm, TurmaForm, TurmaAlunoForm


# Mixin para busca e paginação
class SearchListView(ListView):
    paginate_by = 10
    search_param = "q"

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get(self.search_param, "").strip()
        if q:
            return qs.filter(self.search_filter(q))
        return qs

    def search_filter(self, q):
        return Q()  # Override nas subclasses


# ============================
# Aluno
# ============================
class AlunoListView(SearchListView):
    model = Aluno
    template_name = "alunos/list.html"
    search_param = "q"

    def search_filter(self, q):
        return Q(nome__icontains=q) | Q(email__icontains=q) | Q(cpf__icontains=q)


class AlunoCreateView(CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = "alunos/form.html"
    success_url = reverse_lazy("escola:listar_aluno")

    def form_valid(self, form):
        messages.success(self.request, "Aluno criado com sucesso!")
        return super().form_valid(form)


class AlunoUpdateView(UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = "alunos/form.html"
    success_url = reverse_lazy("escola:listar_aluno")

    def form_valid(self, form):
        messages.success(self.request, "Aluno atualizado com sucesso!")
        return super().form_valid(form)


class AlunoDeleteView(DeleteView):
    model = Aluno
    template_name = "alunos/confirm_delete.html"
    success_url = reverse_lazy("escola:listar_aluno")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Aluno removido.")
        return super().delete(request, *args, **kwargs)


# ============================
# Turma
# ============================
class TurmaListView(SearchListView):
    model = Turma
    template_name = "turma/list.html"

    def search_filter(self, q):
        return Q(nome__icontains=q) | Q(conteudo__icontains=q)


class TurmaCreateView(CreateView):
    model = Turma
    form_class = TurmaForm
    template_name = "turma/form.html"
    success_url = reverse_lazy("escola:listar_turma")

    def form_valid(self, form):
        messages.success(self.request, "Turma criada com sucesso!")
        return super().form_valid(form)


class TurmaUpdateView(UpdateView):
    model = Turma
    form_class = TurmaForm
    template_name = "turma/form.html"
    success_url = reverse_lazy("escola:listar_turma")

    def form_valid(self, form):
        messages.success(self.request, "Turma atualizada!")
        return super().form_valid(form)


class TurmaDeleteView(DeleteView):
    model = Turma
    template_name = "turma/confirm_delete.html"
    success_url = reverse_lazy("escola:listar_turma")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Turma removida.")
        return super().delete(request, *args, **kwargs)


# ============================
# TurmaAluno (vínculo)
# ============================
class TurmaAlunoListView(SearchListView):
    model = TurmaAluno
    template_name = "turma_aluno/list.html"
    paginate_by = 10

    def search_filter(self, q):
        return Q(aluno__nome__icontains=q) | Q(turma__nome__icontains=q)


class TurmaAlunoCreateView(CreateView):
    model = TurmaAluno
    form_class = TurmaAlunoForm
    template_name = "turma_aluno/form.html"
    success_url = reverse_lazy("escola:listar_turma_aluno")

    def form_valid(self, form):
        messages.success(self.request, "Vínculo criado!")
        return super().form_valid(form)


class TurmaAlunoUpdateView(UpdateView):
    model = TurmaAluno
    form_class = TurmaAlunoForm
    template_name = "turma_aluno/form.html"
    success_url = reverse_lazy("escola:listar_turma_aluno")

    def form_valid(self, form):
        messages.success(self.request, "Vínculo atualizado!")
        return super().form_valid(form)


class TurmaAlunoDeleteView(DeleteView):
    model = TurmaAluno
    template_name = "turma_aluno/confirm_delete.html"
    success_url = reverse_lazy("escola:listar_turma_aluno")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Vínculo removido.")
        return super().delete(request, *args, **kwargs)


class TurmaAlunoUpdateView(UpdateView):
    model = TurmaAluno
    form_class = TurmaAlunoForm
    template_name = "turma_aluno/form.html"
    success_url = reverse_lazy("escola:listar_turma_aluno")

    def form_valid(self, form):
        messages.success(self.request, "Vínculo atualizado!")
        return super().form_valid(form)


class TurmaAlunoDeleteView(DeleteView):
    model = TurmaAluno
    template_name = "turma_aluno/confirm_delete.html"
    success_url = reverse_lazy("escola:listar_turma_aluno")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Vínculo removido.")
        return super().delete(request, *args, **kwargs)
