from pessoa import *

joao = Pessoa("Joao da Silva", "Casa 9", "3541-1230")
print(joao.nome, ",", joao._endereco, ",", joao.telefone)

x = 4
print("tipo de um número inteiro:", x.__class__)
print("tipo da classe pessoa:", joao.__class__)
print("dados disponíveis na classe Pessoa:", Pessoa.__dict__)
#print(dir(Pessoa))
print(dir(joao))
print("dados disponíveis na instãncia joao:", joao.__dict__)
#print(joao._ultimo_nome())