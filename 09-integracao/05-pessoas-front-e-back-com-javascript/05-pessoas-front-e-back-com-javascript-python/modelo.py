from peewee import *
import os

arq = './pessoas-front-end.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Pessoa(BaseModel):
    nome = CharField()
    endereco = CharField()
    telefone = CharField()
    
if __name__ == "__main__":
    # apagar o arquivo caso ele exista
    if os.path.exists(arq):
        os.remove(arq)

    db.connect()
    db.create_tables([Pessoa])
    joao = Pessoa.create(nome="Joao da Silva", 
        endereco="Casa 9", telefone="3541-1230")
    maria = Pessoa.create(nome = "Maria de Oliveira", 
        endereco = "Beco das Flores, S/N", telefone="não possui")
    print(joao.nome, ",", joao.endereco, ",", joao.telefone)
