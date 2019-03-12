class Espelho:
    def __init__(self, largura=0, altura=0):
        self.largura = largura
        self.altura = altura

class Casa:
    def __init__(self, quartos=0, cor="branca"):
        self.quartos=quartos
        self.cor = cor
        self.esp = None
    def __str__(self):
        s = "Casa de "+str(self.quartos)+\
            " quartos, "+ self.cor
        if self.esp:
            s += ", com espelho de "+\
                str(self.esp.altura)+" por "+\
                str(self.esp.largura)+" (centímetros)"
        return s

e = Espelho(20, 30)
c = Casa(3, "azul")
c.esp = e
print(c)