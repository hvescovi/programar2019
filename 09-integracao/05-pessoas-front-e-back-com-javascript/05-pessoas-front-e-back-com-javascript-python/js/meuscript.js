$("#btn_listar_pessoas").click(function() {
    $.ajax({
        url: 'http://localhost:4999/listar_pessoas',
        method: 'GET',
        dataType: 'json',
        success: function(resultado) {
            //alert(resultado);
            $('#tabela_pessoas').empty()
            pessoas = resultado.lista;
            var cabecalho = '<div class="rTableRow">' +
                '<div class="rTableHead">Nome</div>' +
                '<div class="rTableHead">Endereço</div>' +
                '<div class="rTableHead">Telefone</div>' +
                '<div class="rTableHead">excluir</div>'
                '</div>';
            $('#tabela_pessoas').append(cabecalho);
            for (var i in pessoas) { //i vale a posição no vetor
                $('#tabela_pessoas').append(ajustar_pessoa_em_linha_de_tabela(pessoas[i]));
            }
        },
        error: function(resultado) {
            alert("ocorreu algum erro na leitura dos dados: ", res);
        }
    });
});

$("#btn_form_incluir_pessoa").click(function() {
    $("#html_form_incluir_pessoa").css("display", "inline-block");
});

$("#btn_incluir_pessoa").click(function() {

    // obtém os dados
    var nome = $("#nome").val();
    var end = $("#endereco").val();
    var tel = $("#telefone").val();
    // prepara os dados em json
    var dados = JSON.stringify({ nome: nome, endereco: end, telefone: tel })

    $.ajax({
        url: 'http://localhost:4999/incluir_pessoa',
        type: 'POST',
        dataType: 'json', // vou receber em json,
        data: dados, //JSON.stringify({ "message": "ok" }), // dados a enviar
        //contentType: "application/json",
        success: function(resultado) {
            //alert(resultado)
            //alert(resultado.message)
            //alert(resultado.details)
            var deu_certo = resultado.message == "ok"
            mostrar_resultado_acao(deu_certo)
        },
        error: function(resultado) {
            alert("ocorreu algum erro na leitura dos dados: ", resultado);
        }
    });

});

function mostrar_resultado_acao(sucesso) {
    if (sucesso) {
        $("#success").fadeIn(1000);
    } else {
        $("#error").fadeIn(1000);
    }
}

function ajustar_pessoa_em_linha_de_tabela(obj_pessoa) {

    var resp = '<div class="rTableRow">' +
        '<div class="rTableCell">' + obj_pessoa.nome + '</div>' +
        '<div class="rTableCell">' + obj_pessoa.endereco + '</div>' +
        '<div class="rTableCell">' + obj_pessoa.telefone + '</div>' +
        '<div class="rTableCell"><img class=excluir_pessoa id=excp_'+obj_pessoa.id+' src=/img/excluir.gif width=20 border=0</div>' +
        '</div>';
    return resp;
}

//$("img").click(function() {
$(document).on("click", ".excluir_pessoa", function(){
    // qual link foi clicado? pega o ID da imagem
    var eu = $(this).attr('id');
    // obtém o id da pessoa
    var id_pessoa = eu.substring(5);
    
    $.ajax({
        url: 'http://localhost:4999/excluir_pessoa',
        type: 'GET',
        dataType: 'json', // vou receber em json,
        data: 'id_pessoa='+id_pessoa,
        //contentType: "application/json",
        success: function(resultado) {
            //alert(resultado)
            //alert(resultado.message)
            //alert(resultado.details)
            //var deu_certo = resultado.message == "ok"
            
            //mostrar_resultado_acao(deu_certo)
        },
        error: function(resultado) {
            alert("ocorreu algum erro na leitura dos dados: ", resultado);
        }
    });

});