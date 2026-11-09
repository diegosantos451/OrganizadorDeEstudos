
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CadastroForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        label='E-mail'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        labels = {
            'username': 'Nome de usuário',
        }

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.email = self.cleaned_data['email']

        if commit:
            usuario.save()

        return usuario

from .models import Tarefa


class TarefaForm(forms.ModelForm):

    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'data_conclusao']

        labels = {
            'titulo': 'Nome da atividade',
            'descricao': 'Descrição',
            'data_conclusao': 'Data para concluir',
        }

        widgets = {
            'data_conclusao': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }
