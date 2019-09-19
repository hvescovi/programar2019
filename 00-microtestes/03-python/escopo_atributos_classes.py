class Pessoa:

    cidade = "Blumenau"

    def __init__(self):
        self.nome = ""

if __name__ == "__main__":

    joao = Pessoa()    
    joao.nome = "João da Silva"

    maria = Pessoa()
    maria.nome = "Maria Kurtz"

    print(joao.nome, "mora em", joao.cidade)
    print(maria.nome, "mora em", maria.cidade)
    print(Pessoa.cidade)

    # altera a cidade de todas as pessoas
    joao.cidade = "Timbó"
    Pessoa.cidade = "Indaial"

    print(joao.nome, "mora em", joao.cidade)
    print(maria.nome, "mora em", maria.cidade)
    print(Pessoa.cidade)