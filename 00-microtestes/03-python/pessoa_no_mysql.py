from peewee import *
import os

db = MySQLDatabase(database="hylson", user="root", 
    password="testando", host="localhost", port=33061)

class BaseModel(Model):
    class Meta:
        database = db

class Pessoa(BaseModel):
    nome = CharField()
    endereco = CharField()
    telefone2 = CharField()
    class Meta:
        db_table = "pessoa_no_mysql"
    
if __name__ == "__main__":
    
    db.connect() # conecta-se ao banco de dados
    db.create_tables([Pessoa]) # cria a tabela de pessoas
    joao = Pessoa.create(nome="Joao da Silva", # cria uma pessoa
        endereco="Casa 9", telefone2="3541-1230")
    maria = Pessoa.create(nome = "Maria de Oliveira", # cria outra pessoa
        endereco = "Beco das Flores, S/N", telefone2="não possui")
    print(joao.nome, ",", joao.endereco, ",", joao.telefone2) # exibe os dados de joao