from flask import Flask, render_template

# referência:
# https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
app = Flask(__name__,
           # remover o padrão "/static"
           static_url_path='', 
           # definir que o conteúdo estático está dentro de templates
           static_folder = 'templates') 

@app.route("/")
def hello():
    return render_template('hello.html')
app.run()