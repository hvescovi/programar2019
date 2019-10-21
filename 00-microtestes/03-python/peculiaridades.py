# https://py.checkio.org/blog/10-common-beginner-mistakes-in-python/
# https://www.devmedia.com.br/python-estrutura-condicional-if-else/38217
# https://www.pythonforbeginners.com/basics/string-manipulation-in-python
# https://py.checkio.org/blog/10-common-beginner-mistakes-in-python/

# elif
# if com estrutura similar a um switch case
#
idade = 18 # define-se uma variável de controle
if idade < 12:
    print('criança')
elif idade < 18:
    print('adolescente')
elif idade < 60:
    print('adulto')
else:
    print('idoso')

#
# print
#

# sep e end valem, por padrão: ' ' (espaço) e '\n', respectivamente
print("que", "mensagem", "legal", sep=" :-) ", end='\n\n\nFIM\n')
nome = "Pedro"
print("Nome:", nome) # mostra 'Nome: Pedro'; a vírgula insere um espaço!
print("Nome:"+nome) # mostra: 'Nome:Pedro'

#
# tudo no python são objetos
#
print(type(1)) # <class 'int'>
print(type('oi')) # <class 'str'>

class Pessoa:
    nome = ''
joao = Pessoa()
joao.nome = "João da Silva"
print(type(joao)) # <class '__main__.Pessoa'>

#
# for percorrendo lista com posições numéricas e por elemento
#
pessoas = ['Joao','Maria','Jose','Hans'] # lista a percorrer

# percorrendo a lista por posição numérica
tamanho_lista = len(pessoas) # obtém o tamanho da lista
# i varia de zero até o tamanho da lista menos 1 (de zero a 3 neste exemplo)
# equivalente a range(0, tamanho_lista)
for i in range(tamanho_lista): 
    print("Mostrando:",pessoas[i])

# percorrendo a lista por elemento (sem informação de posição)
for atual in pessoas: # cada pessoa será mapeada na variável ``atual''
    print("Exibindo:",atual)  

# o range captura desde o valor inicial até o valor final menos 1
# exibir: 0, 1, 2, 3, 4
for i in range(0, 5):
    print(i) 

# fazer uma lista com 5 números
print(list(range(0, 5))) # [0, 1, 2, 3, 4]

# faixa com passo negativo
print(list(range(10, 1, -2))) # [10, 8, 6, 4, 2]

#
# while, break, continue
#
i = 0
while i < 20: 
    i+=1 # python não suporta i++ ou ++i
    print("\nanalisando:",i, end='') # imprime sem EOF
    info = "" # informações a serem mostradas
    if i % 17 == 0: # interrompe se for divisível por 13
        print(" FIM")
        break
    elif i == 7: # é o 7? especial!
        print(" !!! ESPECIAL: é o 7!!!", end='') # mostra pois vai pular o fim do laço
        continue
    elif i % 2 == 0: # é divisível por 2?
        info += " [é par!]"
    else:
        info = " ok"
    print(info, end='')

#
# manipulação de strings
#
frase = "Esta.frase.vai.ser.mostrada.em.partes"
print(frase[0]) # mostra o primeiro caracter da frase
print(frase[:10]) # mostra 10 primeiros caracteres
print(frase[-9:]) # mostra os 9 últimos caracteres
print(frase[::3]) # mostra caracteres saltando a cada 3
print(frase.split(".")) # converte para lista quebrada por "."
print(frase.find("frase")) # mostra a posição da palavra "frase"
print(frase.replace(".","+")) # substitui ponto por soma
print(frase * 2) # mostra a frase duas vezes
print(2 + 2,"=> isso é um número!")
print("2" + "2", "=> isso é uma string")
print("Tamanho da frase:", len(frase))
print("Quantos pontos tem na frase?", frase.count("."))
print(" ".join(frase)) # insere um espaço entre cada caracter da frase

#
# formatação de strings
# https://www.python-course.eu/python3_formatted_output.php
# 
s = "Pedro tem {0:.2f} metros de altura".format(1.7321)
print(s)

cpf = 123456789 # cpf como número :-/
s = "Mariana tem CPF {cpf:011d} e tirou {nota:2.1f} em inglês".format(cpf=cpf,nota=7.12)
p = str(cpf) # converte para string
y = p[-11:-8],p[-8:-5],p[-5:-2] # converte para tupla; resultado: ('1', '234', '567')
x = ".".join(y) + "-" + p[-2:] # insere "." antes de cada elemento de y, depois concatena
print(x) # 1.234.567-89

#
# listas, tuplas, strings, tipos mutáveis e imutáveis
#
lista = [] # lista vazia
lista = [1, 2, 3]
tupla = () # tupla vazia
n = (1+2) # n não é uma tupla!
print(n) # 3
t = (1+2,) # precisa da vírgula para que t seja uma tupla
print(t) # (3,)
tupla = (1, 2, 3)
tupla = 4, 5, 6 # definindo tuplas apenas com vírgulas! tupla = (4, 5, 6)
print(tuple(lista)) # convertendo: (1, 2, 3)
print(list(tupla)) # converteu de novo: [4, 5, 6]

def inclui_na_lista_e_mostra(elemento, lista):
    lista.append(elemento)
    print(lista)
    return lista

lista = inclui_na_lista_e_mostra("Primeiro", [])
lista = inclui_na_lista_e_mostra("Segundo", lista)
inclui_na_lista_e_mostra("Terceiro", lista)

# define função sem retorno
def inclui_e_mostra(elemento, lista):
  lista.append(elemento) # continua modificando a lista por referência
  print(lista)

lista = [] # lista é MUTÁVEL
inclui_e_mostra("Primeiro", lista)
inclui_e_mostra("Segundo", lista)
inclui_e_mostra("Terceiro", lista)

tupla = () # tupla é IMUTÁVEL
try:
    tupla.append("Primeiro")
    print("Consegui inserir na tupla!")
except:
    print("Não foi possível inserir na tupla")

frase = "O amanhã sempre vem" # string é IMUTÁVEL
print(frase)
print(frase.replace("vem", "virá"))
print(frase) # a frase permanece original!

lista = ['lembrando: ','listas ','são ','mutáveis, ','cuidado']
print(lista)
print(lista.remove("são ")) # o método remove não retorna valor (mostra "None")
print(lista) # o elemento foi removido!

a = "Pedro"
b = a # copiou, e não referenciou, pois string é imutável!
b = "Maria"
print(a, b)

lista = [1, 2, 3]
outra = lista # referenciou, pois lista é mutável!
outra.remove(3)
print(outra)
print(lista) # removeu da lista também!

lista = ['a', 'b', 'c']
outra = lista.copy() # copiou um tipo mutável
outra.remove('b')
print(outra)
print(lista)

# tudo certo abaixo
lista = ['lobo','tubarao']
def adicionar_perfil(elemento, conjunto):
    conjunto.append(elemento)
    return conjunto
lista = adicionar_perfil('aguia', lista)
print(lista) # ['lobo', 'tubarao', 'aguia']
lista = adicionar_perfil('gato', lista)
print(lista) # ['lobo', 'tubarao', 'aguia', 'gato']

# porém...
def incluir_perfil(elemento, conjunto=[]): # o parâmetro conjunto é opcional
    conjunto.append(elemento)
    return conjunto
print(incluir_perfil('lobo'))
print(incluir_perfil('tubarao'))
print(incluir_perfil('aguia'))
print(incluir_perfil('gato'))

# o valor padrão do parâmetro é avaliado em tempo de definição,
# e assim considera-se a mesma referência para o mesmo,
# desde a primeira vez que a função é utilizada
# além disso, o parâmetro é MUTÁVEL!

# o mesmo não ocorre para tuplas (imutáveis), já que é preciso
# criar outras referências (conversões)
def incluir_animal(elemento, conjunto=()):
    l = list(conjunto)
    l.append(elemento)
    return tuple(l)
print(incluir_animal('lobo')) # ('lobo',)
print(incluir_animal('tubarao')) # ('tubarao',)

# se informar o parâmetro opcional, ok!
def adicionar_animal(elemento, conjunto=()):
    l = list(conjunto)
    l.append(elemento)
    return tuple(l)
print(incluir_animal('tubarao',('lobo',))) # ('lobo', 'tubarao')
print(incluir_animal('aguia',('lobo','tubarao'))) # ('lobo', 'tubarao', 'aguia')

#
# escopo de variáveis
#
sorte = 7
def numero_da_sorte():
    return sorte
print(numero_da_sorte()) # 7

def mudar_numero_da_sorte():
    sorte = 13 # criou outra variável local chamada sorte
print(numero_da_sorte()) # 7
mudar_numero_da_sorte()
print(numero_da_sorte()) # 7!!!

azar = 15
def mostrar_numero_azar():
    print(azar) 
mostrar_numero_azar() # 15

try:
    azar = 8
    def tentar_mostrar_numero_azar():
        print(azar) # erro: usando variável local antes da definição
        azar = 13 # tenta consertar o número do azar :-)
    tentar_mostrar_numero_azar()
except:
    print("ERRO!")

# => python interpreta declaração por declaração, e não linha por linha
# usar global é uma saída, é não é uma boa ideia

mundo = "belo"
def mostrar_mundo():
    print(mundo) # mostra o mundo
    global mundo
    mundo = "grande" # munda o mundo 
mostrar_mundo() # belo
mostrar_mundo() # grande

# 
# variáveis de classe com herança!
#
class Pai:
    ts = "AB+" # tipo sanguíneo
    def __str__(self): # método para obter a classe em forma de string
        return self.ts
class Filho(Pai):
    pass      # declaração nula, apenas pra concluir a classe

joao = Pai()
zezinho = Filho()
pedrinho = Filho()
pedrinho.ts = "A-"

print(joao, zezinho, pedrinho) # AB+, AB+, A-

pedrinho.ts = "A+"
print(joao, zezinho, pedrinho) # AB+, AB+, A+

joao.ts = "O+" # mudou o tipo do pai
print(joao, zezinho, pedrinho) # O+, AB+, A+

Pai.ts = "O+" # mudou o tipo da CLASSE pai!!
print(joao, zezinho, pedrinho) # O+, O+, A+

#
# diversos
#
# exit(): interrompe um programa!
# pep8: leitura complementar: https://www.python.org/dev/peps/pep-0008/
