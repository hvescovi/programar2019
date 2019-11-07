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

# curl -d '{"nome":"joao"}' -X POST http://localhost:4999/incluir_pessoa
@app.route('/incluir_pessoa', methods=['post'])
def incluir_pessoa():
    # prepara a resposta padrão otimista
    response = jsonify({"message": "ok","details":"ok"})
    try:
        # pega os dados informados
        dados = request.get_json(force=True)
        # cria uma pessoa
        Pessoa.create(nome = dados['nome'], 
            endereco = dados['endereco'], 
            telefone = dados['telefone'])
    except Exception as e:
        # resposta de erro
        response = jsonify({"message": "error","details":str(e)})
        
    # informa que outras origens podem acessar os dados desde servidor/serviço
    response.headers.add('Access-Control-Allow-Origin', '*')
    # retorno!
    return response

@app.route('/excluir_pessoa')
def excluir_pessoa():
    # obtém o id da pessoa
    id_pessoa = request.args.get('id_pessoa')
    # apaga a pessoa
    Pessoa.delete_by_id(id_pessoa)
    # prepara a resposta
    response = jsonify({"message": "ok"})
    # informa que outras origens podem acessar os dados desde servidor/serviço
    response.headers.add('Access-Control-Allow-Origin', '*')
    # retorno!
    return response

app.run(debug=True, port=4999)