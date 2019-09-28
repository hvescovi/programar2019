from flask import Flask, jsonify, json
from modelo import Pessoa
from playhouse.shortcuts import model_to_dict

from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app) #, resources={r"/foo": {"origins": "http://localhost:4999"}})

@app.route("/")
#@cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
def inicio():
    return "backend do sistema de pessoas; <a href=/listar_pessoas>API listar pessoas</a>"

@app.route("/listar_pessoas")
#@cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
def listar_pessoas():
    # forma alternativa rápida: usando map (lambda)
    pessoas = list(map(model_to_dict, Pessoa.select()))
    # liberar a resposta para domínios diferentes do servidor
    #response.headers.add("Access-Control-Allow-Origin", "*")

    '''response = app.response_class(
        response=jsonify({'lista':pessoas}),
        status=200,
        mimetype='application/json'
    )'''

    response = app.response_class(
        response=json.dumps('message:{"hello"}'),
        #response=jsonify("hello"),
        status=200,
        mimetype='application/json'
    )

    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

  #  resposta = jsonify({'lista':pessoas})
  #  resposta.headers.add('Access-Control-Allow-Origin', '*')
  #  return resposta  # referência: https://www.geeksforgeeks.org/python-map-function/

app.run(debug=True,port=4999)

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