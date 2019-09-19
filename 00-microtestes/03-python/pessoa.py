class Pessoa:

    def __init__(self, nome="", end="", tel=""):
        self.nome = nome
        self._endereco = end # atributo 'privado', por convenção
        self.telefone = tel
    
    def _ultimo_nome(self):
        return self.nome.split()[-1]
    
if __name__ == "__main__":
    joao = Pessoa("Joao da Silva", "Casa 9", "3541-1230")
    print(joao.nome, ",", joao._endereco, ",", joao.telefone)
    print(joao._ultimo_nome())