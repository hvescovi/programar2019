import os
from peewee import *
import datetime

arq = 'loja-info.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db
        
class Produto(BaseModel):
    descricao = CharField()
    preco = FloatField()    

class Cliente(BaseModel):
    nome = CharField()
    email = CharField()

class Venda(BaseModel):
    data_hora = DateTimeField()
    produtos = ManyToManyField(Produto)
    cliente = ForeignKeyField(Cliente)

# apaga o arquivo, caso exista, para que múltiplas 
# execuções do teste não dupliquem registros
if os.path.exists(arq):
    os.remove(arq)

db.connect()

# cria as tabelas necessárias ao armazenamento de informações das classes
db.create_tables([Produto, Cliente, Venda, Venda.produtos.get_through_model()])

# teste das classes: criação de objetos com valores
prod1 = Produto.create(descricao = "Notebook LG A540", preco = 2500.0)
prod2 = Produto.create(descricao = "Teclado Asus B-5000", preco = 180.0)
cli = Cliente.create(nome = "Manuel Pereira", email = "manupe@gmail.com")
venda = Venda.create(data_hora = datetime.datetime(2019, 6, 12, 8, 40), cliente=cli)
venda.produtos.add(prod1)

# exibição de informações: obter as vendas
vendas = Venda.select()

# listar dados das vendas
for x in vendas:
    print("Data/hora: :"+str(x.data_hora))
    # listar produtos adquiridos na venda
    for prod in x.produtos:
        print(prod.descricao+", R$ "+str(prod.preco))
    # mostrar quem comprou
    print("Comprador: "+x.cliente.nome+", email="+x.cliente.email)