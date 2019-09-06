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

@app.route("/incluir_receita", methods=['post'])
def incluir_receita():
    # inclui receita
    receita = Receita.create(nome=request.form['nome'])
    # repassa para a inclusão de ingredientes
    return render_template("form_editar_ingredientes_da_receita.html", receita=receita)

@app.route("/form_alterar_receita")    
def form_alterar_receita():
    # obtém a receita a ser alterada
    receita_id = request.args.get('receita_id')
    # carrega a receita
    receita = Receita.get_by_id(receita_id)
    # obtém os ingredientes da receita
    ings = IngredienteDaReceita.select().where(IngredienteDaReceita.receita == receita)
    # obtém todos os ingredientes, para escolha na combobox
    todos_ings= Ingrediente.select()
    # encaminha pra página de edição
    return render_template("form_alterar_receita.html", 
        receita = receita, ings = ings, todos_ings = todos_ings)

@app.route("/incluir_ingrediente_na_receita", methods=['post'])
def incluir_ingrediente_na_receita():
    # obtém id da receita
    receita_id = int(request.form['receita_id'])
    # obtém a receita
    receita = Receita.get_by_id(receita_id)
    # obtém o id do ingrediente selecionado
    ingrediente_id = int(request.form['ingrediente_id'])
    # carrega o ingrediente
    ingrediente = Ingrediente.get_by_id(ingrediente_id)
    # obtém a quantidade informada
    quant = request.form['quantidade']
    # adiciona o ingrediente na receita
    IngredienteDaReceita.create(receita = receita, ingrediente = ingrediente, quantidade = quant)
    # encaminha de volta pra tela de edição
    return redirect("/form_alterar_receita?receita_id="+str(receita_id))

@app.route("/alterar_receita", methods=['post'])
def alterar_receita():
    # obtém os dados da receita
    receita_id = request.form['receita_id']
    nome = request.form['nome']
    # altera
    q = (Receita
        .update({Receita.nome: nome})
        .where(Receita.id == receita_id))
    q.execute()
    # encaminhar
    return redirect ("/listar_receitas")

app.run(debug=True)
