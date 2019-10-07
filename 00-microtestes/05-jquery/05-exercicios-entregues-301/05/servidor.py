from flask import Flask, render_template, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['SECRET_KEY'] = 'senhasegura'

@app.route("/<path:path>")
def inicio(path):
    return send_from_directory('.', path)

app.run(debug=True)
