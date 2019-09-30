from flask import Flask, json, jsonify
from flask import request
from flask_cors import CORS
from modelo import Pessoa
from playhouse.shortcuts import model_to_dict

# necessário instalar:
# pip3 install flask_cors

app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods=['GET'])
def inicio():
    response = app.response_class(
        response="backend do sistema de pessoas; <a href=/listar_pessoas>API listar pessoas</a>",
        status=200,
        mimetype='text/plain',
    )
    return response

@app.route('/listar_pessoas')
def post():
    pessoas = list(map(model_to_dict, Pessoa.select()))
    
    print(pessoas)
    '''resp = app.response_class(
        #response=json.dumps(pessoas),
        response = jsonify(pessoas),
        status=200
        #mimetype='application/json'
    )
    resp.headers['Access-Control-Allow-Origin'] = '*'
'''
    response = jsonify({"lista": pessoas})
    response.headers.add('Access-Control-Allow-Origin', '*')
    #response.headers['Access-Control-Allow-Origin'] = '*'
    #resposta = jsonify({'lista':pessoas})
    return response

if __name__ == '__main__':
    app.run(debug=True, port=4999)