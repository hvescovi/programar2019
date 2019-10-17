from flask import Flask, json, jsonify
from flask import request
from modelo import Pessoa
from playhouse.shortcuts import model_to_dict

# inicializa o servidor
app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicio():
    return "backend do sistema de pessoas; <a href=/listar_pessoas>API listar pessoas</a>"

@app.route('/listar_pessoas')
def listar():
    # converte para pessoa para inserir em uma lista json
    pessoas = list(map(model_to_dict, Pessoa.select()))
    # adiciona à lista json um nome
    response = jsonify({"lista": pessoas})
    # informa que outras origens podem acessar os dados desde servidor/serviço
    response.headers.add('Access-Control-Allow-Origin', '*')
    # retorno!
    return response

app.run(debug=True, port=4999)