class Animal:
    def __init__(self):
        print("Animal criado")
    def comer(self):
        print("Animal comendo")
class Gato(Animal):
    def __init__(self):
        print("Gato criado")

a = Animal()
a.comer() 
g = Gato()
g.comer()