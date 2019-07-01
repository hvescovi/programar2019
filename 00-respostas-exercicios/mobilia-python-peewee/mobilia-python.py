# sistema de controle de mobílias
# limitação desta versão: a quantidade de materiais utilizados para 
# construir uma mobília não fica armazenada junto à mobília e/ou pedido

import os, datetime
from peewee import *

# conectar as classes ao banco de dados -----------------------------

# definir o nome do arquivo de dados do SQLite
arq = 'mobilia.db'
# ligar o arquivo do SQLite com a variável definida na linha anterior
db = SqliteDatabase(arq)
# definir classe-pai que utiliza ligação com BD (class Meta)
class BaseModel(Model):
    class Meta:
        database = db

# definir classes de modelo -----------------------------------------

# toda classe deve herdar BaseModel, em vez de Model
# dessa forma, o atributo database da subclasse Meta já estará definido
class Cliente(BaseModel):
    nome = CharField()
    email = CharField()
    telefone = CharField()
    def __str__(self):
        return self.nome+", "+self.email+", "+self.telefone
    
class Material(BaseModel):
    nome = CharField()
    estoque = IntegerField() # metros ou unidades
    def __str__(self):
        return self.nome + ", "+str(self.estoque)+" em estoque"

class Mobilia(BaseModel):
    nome = CharField()
    materiais = ManyToManyField(Material)
    cor = CharField()
    def __str__(self):
        s = "\nMobilia: "+self.nome+", "+self.cor+", feito com: "
        for mat in self.materiais:
            s+= str(mat) + ", "
        return s

class Pedido(BaseModel):
    data =  DateTimeField()
    cliente = ForeignKeyField(Cliente)
    mobilias = ManyToManyField(Mobilia)
    def __str__(self):
        s = "Pedido feito em "+str(self.data)+", por: "+str(self.cliente)
        for mob in self.mobilias:
            s+= str(mob)+  ", "
        return s

# teste das classes: inicializar BD ---------------------------------

# apagar arquivo de banco de dados, caso exista
if os.path.exists(arq):
    os.remove(arq)

# conectar-se ao BD e criar tabelas
db.connect()
db.create_tables([Cliente, Material, Mobilia, 
  Mobilia.materiais.get_through_model(), Pedido, Pedido.mobilias.get_through_model()])

# testar as classes: criar instâncias de objetos --------------------

joao = Cliente.create(nome="Joao da Silva", email="jsilva@gmail.com", telefone="47 9 9200 1020")
madeira = Material.create(nome="Tábua Eucalipto Aplainada 15x220cm Massol", estoque = 20) # 20 tábuas de madeira
parafuso = Material.create(nome="Parafuso Chipboard Philips p/ Madeira 3,5x40 dourado", estoque = 50)
estante = Mobilia.create(nome = "Estante de eucalipto 5 andares", cor = "natural")
# foram utilizados madeira e parafusos
estante.materiais.add(madeira)
estante.materiais.add(parafuso)
# remover do estoque as quantidades utilizadas: 5 tábuas e 20 parafusos
madeira.estoque = madeira.estoque - 5 
parafuso.estoque = parafuso.estoque - 20 
# salvar os dados alterados!
madeira.save()
parafuso.save()
# o pedido foi feito no dia 01/07/2019, às 09:00hs
pedido = Pedido.create(data = datetime.datetime(2019, 7, 1, 9, 0), cliente=joao)
pedido.mobilias.add(estante)

# testar as classes: exibir informações -----------------------------
print(pedido)