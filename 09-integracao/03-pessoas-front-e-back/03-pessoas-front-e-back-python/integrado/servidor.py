from flask import Flask, render_template, request, redirect, session
from modelo import Pessoa
from peewee import *

app = Flask(__name__)

@app.route("/")
def inicio():
    return "sistema de pessoas. <a href=/listar_pessoas>Operação listar</a>"

@app.route("/listar_pessoas")
def listar_pessoas():
    # fornecer a lista de pessoas para a página exibir as pessoas
    return render_template("listar_pessoas.html", lista = Pessoa.select())

app.run(debug=True)
