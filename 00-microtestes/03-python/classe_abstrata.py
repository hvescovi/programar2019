# https://www.python-course.eu/python3_abstract_classes.php

# biblioteca para fornecer classes abstratas
from abc import ABC, abstractmethod
 
class Animal(ABC):     # classe abstrata (herda de ABC)
 
    # esse construtor possui 1 parâmetro (nome do animal)
    def __init__(self, nome):
        self.nome = nome     # atributo de instância da classe Animal

        # é preciso invocar o construtor para executar
        # inicializações necessárias ao controle de classes abstratas
        super().__init__()
    
    # definição de método abstrato: uso de anotação
    @abstractmethod
    def emitir_som(self):      
        pass            # não faz nenhuma ação

# classe filha concreta
class Cachorro(Animal):

    # implementação do método abstrato
    def emitir_som(self):
        return "au au"

# teste da classe concreta
mike = Cachorro("Mike")
print(mike.emitir_som())