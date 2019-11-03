$("#ler_json").click(function () {
    $.ajax({
        url: 'http://localhost:4999/listar_pessoas',
        method: 'GET',
        dataType: 'json',
        success: function (resultado) {
            alert(resultado);
            pessoas = resultado.lista;
            for (var i in pessoas) { //i vale a posição no vetor
                $('#pessoas').append(pessoas[i].nome + "<br>");
            }
        },
        error: function (resultado) {
            alert("ocorreu algum erro na leitura dos dados: ", res);
        }
    });
});

$("#ler_html").click(function () {
    $.ajax({
        url: 'http://localhost:4999/listar_pessoas',
        method: 'GET',
        dataType: 'text',
        success: function (resultado) {
            alert(resultado);
            dados_json = $.parseJSON(resultado); // converter para json
            pessoas = dados_json['lista'];
            for (var i in pessoas) { // i vale a posição no vetor
                $('#pessoas').append(pessoas[i]['nome']+"<br>");
             }
        },
        error: function (resultado) {
            alert("ocorreu algum erro na leitura dos dados: ", res);
        }
    });
});