from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template('pagina.html')

@app.route("/mostrar_selecao")
def mostrar_selecao():
    # obter os estados selecionados
    # como podem ser enviados vários valores sob o mesmo nome, 
    # deve-se obter uma lista
    lista = request.args.getlist('estado')
    # montar o texto de retorno
    s = "Estados selecionados: "
    for e in lista:
        s += e + " "
    s+= "<br><a href=/>Retornar</a>"    
    return s    

app.run(debug=True)
