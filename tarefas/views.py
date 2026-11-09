
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Tarefa
from .forms import TarefaForm

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CadastroForm


def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('/tarefas/')
    else:
        form = CadastroForm()

    return render(request, 'tarefas/cadastro.html', {
        'form': form
    })

@login_required
def lista_tarefas(request):
    tarefas = Tarefa.objects.filter(usuario=request.user)

    return render(request, 'tarefas/lista.html', {
        'tarefas': tarefas
    })


@login_required
def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)

        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.usuario = request.user
            tarefa.save()

            return redirect('lista_tarefas')
    else:
        form = TarefaForm()

    return render(request, 'tarefas/nova_tarefa.html', {
        'form': form
    })


@login_required
def concluir_tarefa(request, tarefa_id):
    if request.method == 'POST':
        tarefa = get_object_or_404(
            Tarefa,
            id=tarefa_id,
            usuario=request.user
        )

        tarefa.concluida = not tarefa.concluida
        tarefa.save()

    return redirect('lista_tarefas')


@login_required
def excluir_tarefa(request, tarefa_id):
    if request.method == 'POST':
        tarefa = get_object_or_404(
            Tarefa,
            id=tarefa_id,
            usuario=request.user
        )

        tarefa.delete()

    return redirect('lista_tarefas')
def inicio(request):
    return render(request, 'tarefas/inicio.html')