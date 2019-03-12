class Carro:
    def __init__(self, marca = ''):
        self.marca = marca

class Funcionario:
    def __init__(self, nome = ''):
        self.nome = nome
    def dirigir(self, carro):
        print(self.nome+" está dirigindo um "+ carro.marca)

fox = Carro("Fox")
joao = Funcionario("Joao")
joao.dirigir(fox)