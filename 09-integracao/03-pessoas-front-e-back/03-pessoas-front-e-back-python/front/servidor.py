from flask import Flask, render_template, request, redirect, jsonify, json
from modelo import Pessoa
import requests
from playhouse.shortcuts import dict_to_model

app = Flask(__name__)

@app.route("/")
def inicio():
    return "frontend do sistema de pessoas. <a href=/listar_pessoas>Operação listar</a>"

@app.route("/listar_pessoas")
def listar_pessoas():
    # obter do backend a lista de pessoas
    dados_pessoas = requests.get('http://localhost:4999/listar_pessoas')
    # converter os dados recebidos para o formato json
    json_pessoas = dados_pessoas.json()
    # inicializar a lista de pessoas
    pessoas = []
    # percorrer as pessoas em json
    for pessoa_em_json in json_pessoas['lista']:
        
        # http://docs.peewee-orm.com/en/latest/peewee/playhouse.html#dict_to_model
        # converter a pessoa em json para pessoa do peewee
        p = dict_to_model(Pessoa, pessoa_em_json)
        # adicionar a pessoa convertida na lista de pessoas
        pessoas.append(p)
    
    # fornecer a lista de pessoas para a página exibir as pessoas
    return render_template("listar_pessoas.html", lista = pessoas)

@app.route("/form_incluir_pessoa")
def abre_formulario_incluir_pessoa():
    return render_template('form_incluir_pessoa.html')

@app.route("/incluir_pessoa", methods=['post'])
def incluir_pessoa():
    # obter os parâmetros do formulário
    nome = request.form["nome"]
    ender = request.form["endereco"]
    tel = request.form["telefone"]
    # elaborar os parâmetros no formato json
    par = {"nome":nome, "endereco":ender, "telefone":tel}
    # solicitar ao backend a criação da pessoa
    req = requests.post(url='http://localhost:4999/incluir_pessoa', json=par)
    # obter a resposta
    resp = req.json()
    if resp['message'] == 'ok':
        msg = "Pessoa incluída com sucesso"
    else:
        msg = "Erro: "+resp['details']
    # encaminhar a resposta para uma página de exibição de mensagens
    return render_template('exibir_mensagem.html', mensagem=msg)

@app.route("/excluir_pessoa")
def excluir_pessoa():
    # obter o nome da pessoa a ser excluída
    id = request.args.get("id")
    # solicitar a exclusão
    req = requests.get('http://localhost:4999/excluir_pessoa?id='+id)
    # obter a resposta
    resp = req.json()
    if resp['message'] == 'ok':
        return redirect("/listar_pessoas")
    else:
        msg = "Erro: "+resp['details']
        # encaminhar a resposta para uma página de exibição de mensagens
        return render_template('exibir_mensagem.html', mensagem=msg)

@app.route("/form_alterar_pessoa")
def form_alterar_pessoa():
    # obter id da pessoa a ser alterada
    id = request.args.get("id")
    # obter a pessoa
    req = requests.get('http://localhost:4999/consultar_pessoa?id='+id)
    # obter a resposta
    resp = req.json()
    if resp['message'] == 'ok':
        # converter a resposta para a pessoa
        p = dict_to_model(Pessoa, resp['data'])
        # encaminhar o fluxo para a página de alteração
        return render_template("form_alterar_pessoa.html", pessoa=p)
    else:
        msg = "Erro: "+resp['details']
        # encaminhar a resposta para uma página de exibição de mensagens
        return render_template('exibir_mensagem.html', mensagem=msg)
   
@app.route("/alterar_pessoa", methods=['post'])
def alterar_pessoa():
    # obter os parâmetros do formulário
    id = request.form['id']
    nome = request.form["nome"]
    ender = request.form["endereco"]
    tel = request.form["telefone"]
    # elaborar os parâmetros no formato json
    par = {"id":id, "nome":nome, "endereco":ender, "telefone":tel}
    # solicitar ao backend a alteração da pessoa
    req = requests.post(url='http://localhost:4999/alterar_pessoa', json=par)
    # obter a resposta
    resp = req.json()
    if resp['message'] == 'ok':
        return redirect("/listar_pessoas")
    else:
        msg = "Erro: "+resp['details']
        # encaminhar a resposta para uma página de exibição de mensagens
        return render_template('exibir_mensagem.html', mensagem=msg)

app.run(debug=True)