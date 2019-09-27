$.ajax({
    // endereço a ser consultado
    url: "http://127.0.0.1:4999/listar_pessoas",
    contentType: 'application/json',
    method: 'GET',
    dataType: 'json',
    // ao obter sucesso, execute a função abaixo
    success: function (result) {
        // converta os dados recebidos em objeto javascript no formato json
        dados = $.parseJSON(result);
        // pegue a lista de pessoas
        pessoas = dados['lista'];
        alert(pessoas);
        // percorra as pessoas
        //for (pessoa in pessoas) {
        // adicione o nome da pessoa na div apropriada
        //    $('#div_pessoas').append(pessoa["nome"]+"<br>");
        //}
    }
});
