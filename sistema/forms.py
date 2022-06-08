
from logging import PlaceHolder
from django import forms
from django.core.validators import MaxValueValidator

from .models import Endereco



  
class EnderecoForm(forms.ModelForm):
    cep = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "oninput" : "changed()",
                "class" : "cep",
                "placeholder" : "Digite apenas números"
            }
        )
        )
    endereco = forms.CharField(max_length=255, required=True)
    complemento = forms.CharField(max_length=50, required=False)
    descricao = forms.CharField(max_length=255, required=False)
    class Meta:
        model = Endereco
        fields = ('__all__')
      