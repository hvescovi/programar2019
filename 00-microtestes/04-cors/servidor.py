import logging

from flask import Flask, json, jsonify
from flask import request
from flask_cors import CORS

#from task_executor import *

app = Flask(__name__)
cors = CORS(app)

@app.route('/check', methods=['GET'])
def hello():
    response = app.response_class(
        response="Server is running!",
        status=200,
        mimetype='text/plain',
    )
    return response


@app.route('/run', methods=['POST'])
def post():
    response = app.response_class(
        response=json.dumps('message:{"hello"}'),
        #response=jsonify("hello"),
        status=200,
        mimetype='application/json'
    )
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5050)