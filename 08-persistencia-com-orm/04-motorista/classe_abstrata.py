# https://www.python-course.eu/python3_abstract_classes.php

# biblioteca para fornecer classes abstratas
from abc import ABC, abstractmethod

from six import with_metaclass

from peewee import *
import os

# conexão com o banco de dados Sqlite
arq = './animal.db'
db = SqliteDatabase(arq)
 
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

class BaseModel(Model):
    class Meta:
        database = db

# classe filha concreta
class Cachorro(with_metaclass(Animal, BaseModel)):

    nome = CharField()
    raca = CharField()

    # implementação do método abstrato
    def emitir_som(self):
        return "au au"

if __name__ == '__main__':

    # apagar o arquivo caso ele exista
    if os.path.exists(arq):
        os.remove(arq)

    db.connect() # conectar-se ao banco de dados
    db.create_tables([Cachorro]) # solicitar a criação das tabelas

    # teste da classe concreta
    mike = Cachorro.create(nome="Bilu", raca = "Chiuaua")
    print(mike.emitir_som())