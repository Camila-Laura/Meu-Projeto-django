from django import forms
from funcionario.models import Funcionarios

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Funcionarios
        fields = ['nome', 'sobrenome', 'cpf', 'tempo_de_servico', 'remuneracao']
        labels = {'nome': 'Nome', 'sobrenome': 'Sobrenome', 'cpf': 'CPF:', 'tempo_de_servico': 'Tempo de Serviço', 'remuneracao': 'Remuneração'}
        
        