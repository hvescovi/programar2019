from peewee import *

# http://docs.peewee-orm.com/en/latest/peewee/database.html#using-sqlite
# a leitura de dados será apenas em memória, 
# temporário, para renderizar os dados
arq = ':memory:'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Pessoa(BaseModel):
    nome = CharField()
    endereco = CharField()
    telefone = CharField()
    
if __name__ == "__main__":
    db.connect()
    db.create_tables([Pessoa])
    joao = Pessoa.create(nome="Joao da Silva", 
        endereco="Casa 9", telefone="3541-1230")
    print(joao.nome, ",", joao.endereco, ",", joao.telefone)