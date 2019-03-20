from flask import Flask, render_template, request
from modelo import Pessoa
app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template('inicio.html')

@app.route("/listar_pessoas")
def listar_pessoas():
    # criar uma lista de pessoas
    pessoas = [
        Pessoa("Mariana Calculets","Rua das Flores","3521-1212"),
        Pessoa("Tiago da Silva", "Beco 9", "99322-1242")
    ]
    # obter o conteúdo da página de listagem de pessoas
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
    # montar uma mensagem de resposta
    s = "Os seguintes dados do formulário foram recebidos: "
    s += nome + ", " + ender + ", " + tel
    s += "<br>O processamento real será feito em próximas aulas.<a href=/listar_pessoas>Continuar</a>"
    return s

app.run(debug=True)
