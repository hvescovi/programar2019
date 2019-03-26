from flask import Flask, render_template, request
from modelo import Pessoa
app = Flask(__name__)

# criar uma lista de pessoas
# esta variável (lista) é acessada em qualquer parte deste programa servidor
pessoas = [
    Pessoa("Mariana Calculets","Rua das Flores","3521-1212"),
    Pessoa("Tiago da Silva", "Beco 9", "99322-1242")
]

@app.route("/")
def inicio():
    return render_template('inicio.html')

@app.route("/listar_pessoas")
def listar_pessoas():
    # fornecer a lista de pessoas para a página exibir as pessoas
    return render_template("listar_pessoas.html", lista = pessoas)

@app.route("/form_incluir_pessoa")
def abre_formulario_incluir_pessoa():
    return render_template('form_incluir_pessoa.html')

@app.route("/incluir_pessoa")
def incluir_pessoa():
    # obter os parâmetros do formulário
    nome = request.args.get("nome")
    ender = request.args.get("endereco")
    tel = request.args.get("telefone")
    # criar uma pessoa
    nova = Pessoa(nome, ender, tel)
    # adicionar a pessoa na lista
    pessoas.append(nova)
    # encaminhar a resposta para uma página de exibição de mensagens
    return render_template('exibir_mensagem.html', mensagem="Pessoa inserida!")

app.run(debug=True)
