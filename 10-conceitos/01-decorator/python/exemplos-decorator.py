#
# decorators em python
#

#
# referência:
# https://www.datacamp.com/community/tutorials/decorators-python
# 

# ------------------------------------------------
# primeiro conceito: associando funções à variáveis
# ------------------------------------------------

# define uma função para incrementar um número
def somar_um(numero):
    return numero+1

# associa a função à uma variável
adicionar_um = somar_um

# chama a função por meio do nome da variável associada
print("função chamada por outro nome ==>", adicionar_um(5))




#
# segundo conceito: definindo funções dentro de funções (funções "locais")
#

# definição de uma função
def incrementar(numero):

    # definição de uma função "local" (dentro de outra função)
    def somar_um(num):
        
        # impressão sem quebra de linha
        print("função local! ==>", end='')

        # retorno da função "local"
        return num+1

    # chamada da função "local"
    return somar_um(numero)

# chamada da função
print(incrementar(10))



#
# terceiro conceito: passando funções como parâmetro
#

# define uma função que executa outra função
def executar_funcao(qual_funcao):

    # define um valor
    numero = 20

    # chama a função passada como parâmetro com o valor definido
    return qual_funcao(20)

# exibe o resultado da invocação de uma função especificada por parâmetro
# utilizou-se uma função definida anteriormente (somar_um, da linha 8, e não da linha 28)
print("função parametrizada ==>", executar_funcao(somar_um))





#
# quarto conceito: retornando funções geradas em outras funções
#

# definição de uma função que retorna função
def retornar_funcao():

    # criar a função a ser retornada
    def funcao_para_retornar():
        return "olá sou uma função sendo retornada"

    # returnar a função
    return funcao_para_retornar

# obter uma função a partir de outra função    
func = retornar_funcao()

# executar a função retornada
print("executando função retornada ===>", func())





#
# quinto conceito: funções "locais" acessando o exterior da função "externa"
# padrão conhecido como Closure
#

# definir uma função recebendo parâmetro
def recebe_parametro_para_funcao_local(msg):

    # definir uma função local sem parâmetros
    def vou_mostrar():

        # acessa o parâmetro externo à função, e exibe-o
        print(msg)

    # invoca a função local, sem passar o parâmetro
    vou_mostrar()

# invoca a função na qual o parâmetro recebido é exibido pela função local,
# com acesso ao contexto da função
recebe_parametro_para_funcao_local("função com acesso ao contexto ==> acesse o seu contexto e mostre-me")



#
# sexto conceito: padrão de projeto Decorators
#

# definindo um decorator que converte para maiúsculas
# note que o parâmetro do decorator é uma função
def decorator_maiusculas(funcao):

    # define uma função local para realizar a tarefa proposta pelo decorator
    # (wrapper)
    def acao():

        # obtém do contexto (Closure) o nome da função, e executa a função
        func = funcao()

        # sabe-se que o resultado é uma string; converte-se para maiúsculas
        maiusculas = func.upper()

        # retorna as maiúsculas
        return maiusculas

    # retorna um vínculo para a função local (não executa a função local!)
    return acao

# define uma função para ser 'decorada'
def obter_nome_joao():
    return 'Joao da Silva'

# decora a função: o nome será mostrado pelo decorator
nome_maiusculo = decorator_maiusculas(obter_nome_joao)

# invoca a função decorada
print("executando função decorada:", nome_maiusculo())



#
# exemplo de decorator com parâmetro
#

# cria o decorator normalmente
def decorator_maiusculas2(funcao):

    # a função que processa o decoro (wrapper) deve aguardar os parâmetros
    def acao_esperando_parametro(qual_nome):

        # executa a função ligada ao decorator, com o parâmetro esperado
        func = funcao(qual_nome)

        # executa a ação adicional do decorator
        maiusculas = func.upper()

        # retorna o resultado
        return maiusculas
    
    # retorna o vínculo com o wrapper
    return acao_esperando_parametro

def obtem_nome(nom):
    return "O nome é: " + nom

# decora a função
nome_maiusculo = decorator_maiusculas2(obtem_nome)

# executa a função decorada
print("função decorada com parâmetro ==>", nome_maiusculo("Maria Oliveira"))




#
# uso de Decorator com o símbolo @
#

# define o decorator
def destaca_frase(func):

    # define o wrapper
    def acao(frase):

        # executa a função com o parâmetro
        res = func(frase)

        # executa a ação do decoro
        res = "*** " + res + "***"

        # returna o resultado decorado
        return res

    # retorna o vínculo do wrapper
    return acao

# define uma função 'decorada'
@destaca_frase
def adiciona_mensagem_para_joao(mensagem):
    # invoca outra função definida anteriormente
    mensagem = obter_nome_joao() + mensagem
    
    return mensagem

# executa a função decorada
print("função decorada com @ ==>", adiciona_mensagem_para_joao(", essa mensagem é importante!"))
