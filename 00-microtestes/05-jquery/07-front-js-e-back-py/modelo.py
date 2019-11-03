from peewee import *
import os

arq = './pessoas-backend.db'
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

    db.connect() # conecta-se ao banco de dados
    db.create_tables([Pessoa]) # cria a tabela de pessoas
    joao = Pessoa.create(nome="Joao da Silva", # cria uma pessoa
        endereco="Casa 9", telefone="3541-1230")
    maria = Pessoa.create(nome = "Maria de Oliveira", # cria outra pessoa
        endereco = "Beco das Flores, S/N", telefone="não possui")
    print(joao.nome, ",", joao.endereco, ",", joao.telefone) # exibe os dados de joao