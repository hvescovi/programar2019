$("#btn_listar_pessoas").click(function() {
    $.ajax({
        url: 'http://localhost:4999/listar_pessoas',
        method: 'GET',
        dataType: 'json',
        success: function(resultado) {
            $('#tabela_pessoas').empty()
            pessoas = resultado.lista;
            var cabecalho = '<div class="rTableRow">' +
                '<div class="rTableHead">Nome</div>' +
                '<div class="rTableHead">Endereço</div>' +
                '<div class="rTableHead">Telefone</div>' +
                '<div class="rTableHead"></div>' +
                '<div class="rTableHead"></div>' +
                '</div>';
            $('#tabela_pessoas').append(cabecalho);
            for (var i in pessoas) { //i vale a posição no vetor
                lin = '<div class="rTableRow" id=linha' + pessoas[i].id + '>'+
                      ajustar_pessoa_em_linha_de_tabela(
                    pessoas[i].id, pessoas[i].nome, pessoas[i].endereco, pessoas[i].telefone) +
                    '</div>';
                $('#tabela_pessoas').append(lin);
            }
        },
        error: function() {
            alert("ocorreu algum erro na leitura dos dados, verifique o backend");
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
            var deu_certo = resultado.message == "ok";
            mostrar_resultado_acao(deu_certo);
            if (!deu_certo) {
                alert(resultado.message + ":" + resultado.details);
            }

        },
        error: function() {
            alert("ocorreu algum erro na leitura dos dados, verifique o backend");
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

function ajustar_pessoa_em_linha_de_tabela(id, nome, endereco, telefone) {

    var resp = '<div class="rTableCell" id="nome' + id + '">' + nome + '</div>' +
        '<div class="rTableCell" id="endereco' + id + '">' + endereco + '</div>' +
        '<div class="rTableCell" id="telefone' + id + '">' + telefone + '</div>' +
        '<div class="rTableCell"><img class=form_alterar_pessoa id=altp_' + id + ' src=img/alterar.png width=20 border=0></div>' +
        '<div class="rTableCell"><img class=excluir_pessoa id=excp_' + id + ' src=img/excluir.gif width=20 border=0></div>';
    return resp;
}

$(document).on("click", ".excluir_pessoa", function() {
    // qual link foi clicado? pega o ID da imagem
    var eu = $(this).attr('id');
    // obtém o id da pessoa
    var id_pessoa = eu.substring(5);

    $.ajax({
        url: 'http://localhost:4999/excluir_pessoa',
        type: 'GET',
        dataType: 'json', // vou receber em json,
        data: 'id_pessoa=' + id_pessoa,
        //contentType: "application/json",
        success: function(resultado) {
            var deu_certo = resultado.message == "ok"

            if (!deu_certo) {
                alert(resultado.message + ":" + resultado.details);
            } else {
                // remove a linha
                $("#linha" + id_pessoa).hide(1000);
            }
        },
        error: function() {
            alert("ocorreu algum erro na leitura dos dados, verifique o backend");
        }
    });
});

function ajustar_pessoa_em_linha_de_tabela_modo_edicao(id_pessoa) {

    var nome = $("#nome" + id_pessoa).text();
    var end = $("#endereco" + id_pessoa).text();
    var tel = $("#telefone" + id_pessoa).text();

    var resp = '<div class="rTableCell"><input type=text id=novo_nome' + id_pessoa + ' size=10 value="' + nome + '"></div>' +
        '<div class="rTableCell"><input type=text id=novo_endereco' + id_pessoa + ' size=10 value="' + end + '"></div>' +
        '<div class="rTableCell"><input type=text id=novo_telefone' + id_pessoa + ' size=10 value="' + tel + '"></div>' +
        '<div class="rTableCell"><img class=acao_alterar_pessoa id=alterar' + id_pessoa + ' src=img/success.gif width=20 border=0></div>' +
        '<div class="rTableCell"><img class=acao_cancelar_alterar_pessoa id=cancelar' + id_pessoa + ' src=img/cancelar.png width=20 border=0></div>';

    return resp;
}

$(document).on("click", ".form_alterar_pessoa", function() {
    // qual link foi clicado? pega o ID da imagem
    var eu = $(this).attr('id');
    // obtém o id da pessoa
    var id_pessoa = eu.substring(5); // altp_ID
    // preenche a div da linha com dados editáveis
    $("#linha" + id_pessoa).html(ajustar_pessoa_em_linha_de_tabela_modo_edicao(id_pessoa));
});

$('.muda_estilo').click(function() {
    $('#estilo_tabela').attr('href', 'css/' + $(this).attr('id') + '.css');
});

$(document).on("click", ".acao_alterar_pessoa", function() {
    // qual link foi clicado? pega o ID da imagem
    var eu = $(this).attr('id');
    // obtém o id da pessoa
    var id_pessoa = eu.substring(7); // alterarID
    // obtém os dados
    var nome = $("#novo_nome" + id_pessoa).val();
    var end = $("#novo_endereco" + id_pessoa).val();
    var tel = $("#novo_telefone" + id_pessoa).val();

    // prepara os dados em json
    var dados = JSON.stringify({ id: id_pessoa, nome: nome, endereco: end, telefone: tel })

    $.ajax({
        url: 'http://localhost:4999/alterar_pessoa',
        type: 'POST',
        dataType: 'json', // vou receber em json,
        data: dados, //JSON.stringify({ "message": "ok" }), // dados a enviar
        //contentType: "application/json",
        success: function(resultado) {
            var deu_certo = resultado.message == "ok"
            if (!deu_certo) {
                alert(resultado.message + ":" + resultado.details);
            }
            // preenche a div da linha com dados editáveis
            $("#linha" + id_pessoa).html(ajustar_pessoa_em_linha_de_tabela(id_pessoa, nome, end, tel));
        },
        error: function(request, status, error) {
            alert("ocorreu algum erro na leitura dos dados: ", request.responseText);
        }
    });
});