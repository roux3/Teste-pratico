from tkinter.tix import Form
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, CreateView, FormView, UpdateView
from django.core import serializers

from .models import Endereco
from .forms import EnderecoForm

class EnderecoList(ListView):
    model = Endereco

class EnderecoDetail(DetailView):
    model = Endereco

def buscarCep(request):
    cep = request.POST.get('cep')
    query = Endereco.objects.filter(cep=cep)
    resposta = None
    if len(query) > 0 and len(cep) > 0:
        data = []
        for i in query:
            item = {
                'endereco': i.endereco,
                'bairro': i.bairro,
                'cidade': i.cidade,
                'uf': i.uf,
            }
            data.append(item)
        resposta = data
    else:
        resposta = "vazio"

    return JsonResponse({'data': resposta})

class AtualizarEndereco(UpdateView):
    model = Endereco
    form_class = EnderecoForm
    field = ['__all__']
    template_name = "endereco_form.html"
    success_url = '/'

class CadastroEndereco(CreateView):
    model = Endereco
    form_class = EnderecoForm
    success_url = '/'



def atualizarEndereco(request):
    cep = request.POST.get('cep')
    objeto = Endereco.objects.get(cep=cep)
    if( request.method == 'POST'):
        form = EnderecoForm(request.POST or None, instance=objeto)
        form.save()
        return redirect("/")
    
    


# Create your views here.
