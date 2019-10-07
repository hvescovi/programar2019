from flask import Flask, render_template, request, session, redirect, url_for
from Classe import Pessoa
from peewee import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "123"

lista = Pessoa.select()

@app.route("/")
def iniciar():
    return render_template("html.html")

@app.route("/listar_pessoas")
def listar_pessoas():
    return render_template("listar_pessoas.html", usuario=lista)

@app.route("/abrir_formulario")
def abrir_formulario():
    return render_template("inserir_pessoas_formulario.html")

@app.route("/cadastrar")
def add():
	codigo = request.args.get("codigo")
	nome = request.args.get("nome")
	endereco = request.args.get("endereco")
	telefone = request.args.get("telefone")
	pessoa = Pessoa(codigo, nome, endereco, telefone)
	nova = Pessoa.create(nome=request.form["nome"])
	return redirect("/mostrar_mensagem")

@app.route("/mostrar_mensagem")
def mostrar_mensagem():
    return render_template("exibir_mensagem.html")

@app.route("/abrir_alterar_pessoas")
def abrir_alterar_pessoas():
	pe = None
	codigo = request.args.get("codigo")
	for pe in lista:
		if pe.codigo == codigo:
			return render_template("alterar_pessoas_form.html", pessoa=pe)
	return "Pessoa não encontrada: " + str(codigo)

@app.route("/alterar_pessoas")
def alterar_pessoas():
	codigo = request.args.get("codigo")
	nome = request.args.get("nome")
	endereco = request.args.get("endereco")
	telefone = request.args.get("telefone")
	nova_pessoa = Pessoa(codigo, nome, endereco, telefone)
	for pessoa in range(len(lista)):
		if lista[pessoa].codigo == codigo:
			lista[pessoa] = nova_pessoa
			return redirect("/listar_pessoas")
	return "Pessoa não encontrada: " + str(nome)

@app.route("/excluir_pessoas")
def excluir_pessoas():
	item = None
	codigo = request.args.get("codigo")
	for user in lista:
		if codigo == user.codigo:
			item = user
			break
	if item != None:
		lista.remove(item)
	return redirect("/listar_pessoas")

@app.route("/form_login")
def form_login():
	return render_template("login_formulario.html")

@app.route("/login", methods=['post'])
def login():
	login = request.form["login"]
	senha = request.form["senha"]
	if login == "administrador" and senha == "587":
		session["Usuário"] = login
		return redirect("/")
	else:
		return "Houve algum erro durante o seu login!"

@app.route("/logout")
def logout():
	session.pop("Usuário")
	return redirect("/")

app.run(debug=True)