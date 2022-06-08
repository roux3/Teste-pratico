from django.urls import URLPattern, path

from . import views

app_name = "sistema"

urlpatterns = [
    path("", views.EnderecoList.as_view(), name="list"),
    path("cadastrar/", views.CadastroEndereco.as_view(), name='cadastro'),
    path("atualizar/", views.atualizarEndereco, name='atualiza'),
    path("buscar/", views.buscarCep, name='busca'),
    

]