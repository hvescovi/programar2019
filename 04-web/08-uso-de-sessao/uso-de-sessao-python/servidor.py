from flask import Flask, render_template, request, redirect, session
from modelo import Pessoa
app = Flask(__name__)
app.config['SECRET_KEY'] = '43r78934yt6y5907'

# criar uma lista de pessoas
# esta variável (lista) é acessada em qualquer parte deste programa servidor
pessoas = [
    Pessoa("Mariana","Rua das Flores","3521-1212"),
    Pessoa("Tiago", "Beco 9", "99322-1242")
]

@app.route("/")
def inicio():
    return render_template('inicio.html')

@app.route("/listar_pessoas")
def listar_pessoas():
    # fornecer a lista de pessoas para a página exibir as pessoas
    return render_template("listar_pessoas.html", lista = pessoas)

@app.route("/form_incluir_pessoa")
def abre_formulario_incluir_pessoa():
    return render_template('form_incluir_pessoa.html')

@app.route("/incluir_pessoa")
def incluir_pessoa():
    # obter os parâmetros do formulário
    nome = request.args.get("nome")
    ender = request.args.get("endereco")
    tel = request.args.get("telefone")
    # criar uma pessoa
    nova = Pessoa(nome, ender, tel)
    # adicionar a pessoa na lista
    pessoas.append(nova)
    # encaminhar a resposta para uma página de exibição de mensagens
    return render_template('exibir_mensagem.html', mensagem="Pessoa inserida!")

@app.route("/excluir_pessoa")
def excluir_pessoa():
    # inicializar uma variável de controle
    excluir = None
    # obter o nome da pessoa a ser excluída
    nome = request.args.get("nome")
    # percorrer a lista de pessoas
    for pessoa in pessoas:
        # se a pessoa a excluir for a atual
        if nome == pessoa.nome:
            # marca a pessoa a ser excluída
            excluir = pessoa
            break

    # encontrou a pessoa para excluir?
    if excluir != None:
        # remove a pessoa da lista
        pessoas.remove(excluir)
    
    # encaminha o fluxo de execução para a página de listagem
    # pode-se invocar a função que lista pessoas
    return listar_pessoas()

@app.route("/form_alterar_pessoa")
def form_alterar_pessoa():
    # obter o nome da pessoa
    nome = request.args.get("nome")
    # percorrer a lista de pessoas
    for pessoa in pessoas:
        # se a pessoa a alterar for a atual
        if nome == pessoa.nome:
            # encaminha o fluxo para a página de alteração
            return render_template("form_alterar_pessoa.html", pessoa=pessoa)
    # caso não encontre a pessoa: retorna para a página de listagem
    return listar_pessoas()

@app.route("/alterar_pessoa")
def alterar_pessoa():
    # obter os dados do formulário de edição de pessoa
    nome = request.args.get("nome")
    endereco = request.args.get("endereco")
    telefone = request.args.get("telefone")
    nome_original = request.args.get("nome_original")
    # sinaliza que ainda não houve busca pela pessoa a ser alterada
    indice = -1
    # percorrer a lista de pessoas usando um índice numérico
    for i in range(len(pessoas)):
        # se a pessoa a alterar for a atual
        if pessoas[i].nome == nome_original:
            # sinaliza que vai haver alteração de dados
            indice = i
            # interrompe a busca, pois o procurado foi encontrado
            break
    # se encontrou o procurado
    if indice >= 0:
        # altera a pessoa para uma nova pessoa, com os dados atualizados
        pessoas[indice] = Pessoa(nome, endereco, telefone)
    # encaminha a execução para a página de listagem de dados
    # é utilizado um redirecionador, para que a URL do navegador
    # seja efetivamente alterada
    return redirect("listar_pessoas")

@app.route("/form_login")
def form_login():
    return render_template("form_login.html")

@app.route("/login")
def login():
    # receber as informações de login e senha
    login = request.args.get("login")
    senha = request.args.get("senha")
    # verificar se a combinação é válida
    if login == 'hvescovi' and senha == '123':
        # sucesso no login: armazena informação na sessão
        session['usuario'] = login
        # encaminha para o menu principal do sistema
        return redirect("/")
    else:
        # informa que o login é inválido
        return render_template("exibir_mensagem", mensagem="Login/senha inválido(s)")

@app.route("/logout")
def logout():
    # remove da sessão a informação de usuário 
    session.pop("usuario")
    # redireciona para o início do sistema
    return redirect("/")

app.run(debug=True)
