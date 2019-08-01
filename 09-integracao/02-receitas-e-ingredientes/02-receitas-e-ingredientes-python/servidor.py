from flask import Flask, render_template, request, redirect
from modelo import *
from peewee import *

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template('inicio.html')

@app.route("/listar_receitas")
def listar_pessoas():
    # fornecer a lista de pessoas para a página exibir as pessoas
    return render_template("listar_receitas.html", receitas = Receita.select())

@app.route("/listar_ingredientes_da_receita")
def listar_ingredientes_da_receita():
    # obtém id da receita
    receita_id = int(request.args.get("receita_id"))
    # obtém a receita
    receita = Receita.get_by_id(receita_id)
    # obtém ingredientes daquela receita
    ings = IngredienteDaReceita.select().where(IngredienteDaReceita.receita == receita)
    # encaminha receita e ingredientes para a página de exibição
    return render_template("listar_ingredientes_da_receita.html", receita=receita, ings=ings)
    
app.run(debug=True)
