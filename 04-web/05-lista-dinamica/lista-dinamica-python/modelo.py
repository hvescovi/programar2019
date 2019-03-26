class Pessoa:

    def __init__(self, nome="", end="", tel=""):
        self.nome = nome
        self.endereco = end
        self.telefone = tel
    
if __name__ == "__main__":
    joao = Pessoa("Joao da Silva", "Casa 9", "3541-1230")
    print(joao.nome, ",", joao.endereco, ",", joao.telefone)
