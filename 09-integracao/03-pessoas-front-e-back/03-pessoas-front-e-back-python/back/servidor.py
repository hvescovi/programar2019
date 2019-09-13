from flask import Flask, jsonify
from modelo import Pessoa
from playhouse.shortcuts import model_to_dict, dict_to_model

app = Flask(__name__)

@app.route("/")
def inicio():
    return "backend do sistema de pessoas; <a href=/listar_pessoas>API listar pessoas</a>"

@app.route("/listar_pessoas")
def listar_pessoas():
    # obter as pessoas do peewee
    pessoas_peewee = Pessoa.select()
    # inicializar a string que vai conter o json
    json = ""
    # percorrer as pessoas
    for p in pessoas_peewee:
        # adicionar a pessoa em versão json
        # https://stackoverflow.com/questions/53850558/return-single-peewee-record-as-dict
        # http://docs.peewee-orm.com/en/latest/peewee/playhouse.html#model_to_dict
        json += str(model_to_dict(p))+" ,"
    # remove a última vírgula sobrando
    j2 = json[:-1]
    # retorna o json
    return jsonify({'lista':j2})

@app.route("/listar_pessoas2")
def listar_pessoas2():
    # forma alternativa rápida: usando map (lambda)
    pessoas = list(map(model_to_dict, Pessoa.select()))
    return jsonify({'lista':pessoas})
    # referência: 
    # https://www.geeksforgeeks.org/python-map-function/
    
''' exemplo do map:

def dobrar(n):
    return n*2
numeros = [1, 2, 3]
resultado = map(dobrar, numeros)
print(resultado)
print(list(resultado))

execução:
<map object at 0x7ff0ca2d6a90>
[2, 4, 6]

'''


'''
exemplo de retorno:
{
  "lista": [
    {
      "endereco": "Casa 9", 
      "id": 1, 
      "nome": "Joao da Silva", 
      "telefone": "3541-1230"
    }, 
    {
      "endereco": "Casa 9", 
      "id": 2, 
      "nome": "Joao da Silva", 
      "telefone": "3541-1230"
    }
  ]
}
'''

app.run(debug=True,port=4999)
