from flask import Flask, render_template, request, redirect, session
from modelo import Pessoa
import requests
from playhouse.shortcuts import model_to_dict, dict_to_model

# https://www.twilio.com/blog/2016/12/http-requests-in-python-3.html
# pip3 install requests
# necessário para fazer chamadas get no python: acessar o backend

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

app.run(debug=True)