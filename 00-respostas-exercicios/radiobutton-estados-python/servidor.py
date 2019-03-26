from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template('inicial.html', estados = retorna_lista_estados())

@app.route("/mostrar_selecao")
def mostrar_selecao():
    # obtem o estado escolhido
    es = request.args.get('estado')
    # retornar a sigla do estado escolhido
    return "Estado selecionado: " + es + "<br><a href=/>Retornar</a>"

def retorna_lista_estados():
    lista = []
    lista.append(("AC", "Acre"))
    lista.append(("AL", "Alagoas"))
    lista.append(("AM", "Amazonas"))
    lista.append(("AP", "Amapa"))
    lista.append(("BA", "Bahia"))
    lista.append(("CE", "Ceará"))
    lista.append(("DF", "Distrito Federal"))
    lista.append(("ES", "Espírito Santo"))
    lista.append(("GO", "Goiás"))
    lista.append(("MA", "Maranhão"))
    lista.append(("MG", "Minas Gerais"))
    lista.append(("MS", "Mato Grosso do Sul"))
    lista.append(("MT", "Mato Grosso"))
    lista.append(("PA", "Pará"))
    lista.append(("PB", "Paraíba"))
    lista.append(("PE", "Pernambuco"))
    lista.append(("PI", "Piauí"))
    lista.append(("PR", "Paraná"))
    lista.append(("RJ", "Rio de Janeiro"))
    lista.append(("RN", "Rio Grande do Norte"))
    lista.append(("RS", "Rio Grande do Sul"))
    lista.append(("RO", "Rondônia"))
    lista.append(("RR", "Roraima"))
    lista.append(("SC", "Santa Catarina"))
    lista.append(("SE", "Sergipe"))
    lista.append(("SP", "São Paulo"))
    lista.append(("TO", "Tocantins"))
    return lista

app.run(debug=True)
