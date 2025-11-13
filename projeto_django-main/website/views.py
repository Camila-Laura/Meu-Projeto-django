from django.shortcuts import render, get_object_or_404
from funcionario.models import Funcionarios
from .forms import FormularioForm
from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
# from django.urls import reverse

# Create your views here.


def index(request):
    return render(request, 'website/index.html')

def cadastrar_funcionario(request):
    if request.method != 'POST':
        form = FormularioForm()
    else:
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'website/cadastrar_funcionario.html', context)
        

def listar_funcionarios(request):
    funcionarios = Funcionarios.objects.all() 
    contexto = {"funcionarios": funcionarios}
    return render(request, 'website/funcionarios.html', contexto)

def detalhes_funcionario(request, id):
    funcionario = get_object_or_404(Funcionarios, pk=id)
    contexto = {"funcionario": funcionario}
    return render(request, 'website/detalhesFuncionario.html', contexto)


def editar_funcionario(request, id):
    funcionario = Funcionarios.objects.get(id=id)

    if request.method == 'POST':
        form = FormularioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('website:listar')  
    else:
        form = FormularioForm(instance=funcionario)

    context = {'form': form, 'funcionario': funcionario}
    return render(request, 'website/editar_funcionario.html', context)


def excluir_funcionario(request, id):
    funcionario = get_object_or_404(Funcionarios, pk=id)
    
    if request.method == "POST":
        funcionario.delete()
        return redirect('website:listar')
    
    return render(request, 'website/excluir_funcionario.html', {'funcionario': funcionario})

def contato(request):
    return render(request, 'website/contato.html')


# def excluir_funcionario(request, id):
#     funcionario = get_object_or_404(Funcionarios, pk=id)
#     if request.method == "POST":
#         funcionario.delete()
#         return redirect('website:listar')  # ou o nome de rota que lista
#     contexto = {"funcionario": funcionario}
#     return render(request, 'website/confirmar_excluir.html', contexto)