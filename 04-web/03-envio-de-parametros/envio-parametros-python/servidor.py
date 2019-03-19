from flask import Flask, render_template
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

app.run(debug=True)
