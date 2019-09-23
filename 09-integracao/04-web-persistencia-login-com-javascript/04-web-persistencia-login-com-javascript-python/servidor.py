from flask import Flask, render_template, request, redirect, session
from modelo import Pessoa
from peewee import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '43r78934yt6y5907'

@app.route("/")
def inicio():
    return render_template('inicio.html')

@app.route("/listar_pessoas")
def listar_pessoas():
    # fornecer a lista de pessoas para a página exibir as pessoas
    return render_template("listar_pessoas.html", lista = Pessoa.select())

@app.route("/form_incluir_pessoa")
def abre_formulario_incluir_pessoa():
    return render_template('form_incluir_pessoa.html')

@app.route("/incluir_pessoa")
def incluir_pessoa():
    # obter os parâmetros do formulário
    nome = request.args.get("nome")
    ender = request.args.get("endereco")
    tel = request.args.get("telefone")
    # criar uma pessoa (não é preciso atribuir a nova pessoa à uma)
    Pessoa.create(nome=nome, endereco=ender, telefone=tel)
    # encaminhar a resposta para uma página de exibição de mensagens
    return render_template('exibir_mensagem.html', mensagem="Pessoa inserida!")

@app.route("/excluir_pessoa")
def excluir_pessoa():
    # obter o nome da pessoa a ser excluída
    id = request.args.get("id")
    # solicitar a exclusão
    Pessoa.delete_by_id(id)
    # encaminhar o fluxo de execução para a página de listagem
    return redirect("/listar_pessoas")

@app.route("/form_alterar_pessoa")
def form_alterar_pessoa():
    # obter id da pessoa a ser alterada
    id = request.args.get("id")
    # obter a pessoa
    pessoa_para_alterar = Pessoa.get_by_id(id)
    # encaminhar o fluxo para a página de alteração
    return render_template("form_alterar_pessoa.html", pessoa=pessoa_para_alterar)
    
@app.route("/alterar_pessoa")
def alterar_pessoa():
    # obter os dados do formulário de edição de pessoa
    id = request.args.get("id")
    nome = request.args.get("nome")
    endereco = request.args.get("endereco")
    telefone = request.args.get("telefone")
    # obter a pessoa original
    cidadao = Pessoa.get_by_id(id)
    # alterar os dados da pessoa
    cidadao.nome = nome
    cidadao.endereco = endereco
    cidadao.telefone = telefone
    # atualizar os dados
    cidadao.save()
    # encaminhar a execução para a página de listagem de dados
    return redirect("/listar_pessoas")

@app.route("/form_login")
def form_login():
    return render_template("form_login.html")

@app.route("/login", methods=['POST'])
def login():
    # receber as informações de login e senha
    login = request.form["login"]
    senha = request.form["senha"]
    # verificar se a combinação é válida
    if login == 'admin' and senha == '123':
        # sucesso no login: armazena informação na sessão
        session['usuario'] = login
        # encaminha para o menu principal do sistema
        return redirect("/")
    else:
        # informa que o login é inválido
        return render_template("exibir_mensagem", mensagem="Login/senha inválido(s)")

@app.route("/logout")
def logout():
    # remove da sessão a informação de usuário 
    session.pop("usuario")
    # redireciona para o início do sistema
    return redirect("/")

# exemplo de login via javascript
@app.route("/exemplo1")
def exemplo1():
    return render_template("exemplo1.html")

# ação que recebe o login diretamente da chamada javascript
@app.route("/prelogin", methods=['POST'])
def prelogin():
    # receber as informações de login e senha
    login = request.form["login"]
    senha = request.form["senha"]
    # verificar se a combinação é válida
    if login == 'admin' and senha == '123':
        return '{"message":"ok"}'
    else:
        return '{"message":"error"}'

app.run(debug=True)
