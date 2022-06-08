
cep = document.getElementsByClassName("cep")[0]
endereco = document.getElementsByName("endereco")[0]
bairro = document.getElementsByName("bairro")[0]
uf = document.getElementsByName("uf")[0]
cidade = document.getElementsByName("cidade")[0]

async function BuscarCep(data){
    endereco = document.getElementsByName("endereco")[0]
    bairro = document.getElementsByName("bairro")[0]
    uf = document.getElementsByName("uf")[0]
    cidade = document.getElementsByName("cidade")[0]
    csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
    var formData = new FormData()
    formData.append("cep", cep.value)
    formData.append("csrfmiddlewaretoken", csrf)

    const response = await fetch('/buscar/',
    {
        method: 'POST',
        body: formData
    });
    var data = await response.json();
    if(data.data == "vazio"){
        
        api()
    }
    else{
        form = document.getElementById("formId")
        //form.method = "put"
        form.action = "/atualizar/"
        dado = data.data[0]
        endereco.value = dado.endereco
        bairro.value = dado.bairro
        cidade.value = dado.cidade
        uf.value = dado.uf
    }

}

function changed(){
    cep = document.getElementsByClassName("cep")[0]
    if(cep.value.length == 8){
        BuscarCep(cep.value)
    }
}


async function api(){
    url = `https://viacep.com.br/ws/${cep.value}/json/`
    form = document.getElementById("formId")
    form.action = "/cadastrar/"  

         
        const response = await fetch(url);
        var data = await response.json();
        if(data.localidade != undefined){
            endereco.value = data.logradouro
            bairro.value = data.bairro
            cidade.value = data.localidade
            uf.value = data.uf
        }

}