from flask import Flask, jsonify, request
from modelo import Pessoa
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)

@app.route("/")
def inicio():
    return "backend do sistema de pessoas; <a href=/listar_pessoas>API listar pessoas</a>"

@app.route("/listar_pessoas")
def listar_pessoas():
    # forma alternativa rápida: usando map (lambda)
    pessoas = list(map(model_to_dict, Pessoa.select()))
    return jsonify({'lista':pessoas})

@app.route("/incluir_pessoa", methods=['post'])
def incluir_pessoa():
    # preparar mensagem de retorno padrão (sucesso)
    msg = jsonify({"message":"ok"})
    # obter os dados
    dados = request.get_json(force=True)
    # obter os valores
    nome = dados['nome']
    ender = dados['endereco']
    tel = dados['telefone']
    # criar a nova pessoa
    Pessoa.create(nome=nome, endereco=ender, telefone=tel)
    return msg

@app.route("/excluir_pessoa")
def excluir_pessoa():
  # preparar mensagem de retorno padrão (sucesso)
  msg = jsonify({"message":"ok"})
  # obter o id
  id = request.args.get("id")
  # exclui
  Pessoa.delete_by_id(id)
  return msg
   
@app.route("/alterar_pessoa", methods=['post'])
def alterar_pessoa():
    # preparar mensagem de retorno padrão (sucesso)
    msg = jsonify({"message":"ok"})
    # obter os dados
    dados = request.get_json(force=True)
    # obter os dados da pessoa a ser alterada
    id = dados['id']
    nome = dados['nome']
    ender = dados['endereco']
    tel = dados['telefone']
    # obter a pessoa original
    cidadao = Pessoa.get_by_id(id)
    # alterar os dados da pessoa
    cidadao.nome = nome
    cidadao.endereco = ender
    cidadao.telefone = tel
    # atualizar os dados
    cidadao.save()
    return msg

@app.route("/consultar_pessoa")
def consultar_pessoa():
    # preparar mensagem de retorno padrão (sucesso)
    msg = jsonify({"message":"error","detail":"iniciando procedimentos"})
    # obter o id
    id = request.args.get("id")
    # obter a pessoa original
    cidadao = Pessoa.get_by_id(id)
    # preparar retorno
    msg = jsonify({"message":"ok","detail":"ok","data":model_to_dict(cidadao)})
    return msg    

app.run(debug=True,port=4999)