from django import forms
from django.forms import ModelForm

from .models import Pessoas


class PessoasForm(ModelForm):

    pesso_nome = forms.Textarea()

    class Meta:
        model = Pessoas
        fields = ["pess_nome"]
