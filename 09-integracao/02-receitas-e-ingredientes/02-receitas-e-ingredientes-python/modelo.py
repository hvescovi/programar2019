from peewee import *
import os

arq = '/home/friend/receitas-e-ingredientes.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Receita(BaseModel):
    nome = CharField()
class Ingrediente(BaseModel):
    nome = CharField()
    unidade = CharField()
class IngredienteDaReceita(BaseModel):
    receita = ForeignKeyField(Receita)
    ingrediente = ForeignKeyField(Ingrediente)
    quantidade = FloatField()

if __name__ == "__main__":
    # preliminares
    if os.path.exists(arq):
        os.remove(arq)
    db.connect()
    db.create_tables([Receita, Ingrediente, IngredienteDaReceita])
    
    # criações de objetos
    bolo = Receita.create(nome = "Bolo de laranja")
    ovo = Ingrediente.create(nome = "Ovo", unidade = "unidade")
    xicoleo = Ingrediente.create(nome = "Óleo", unidade = "xícara")
    ing1 = IngredienteDaReceita.create(receita = bolo,
    ingrediente = ovo, quantidade = 4.0)
    ing2 = IngredienteDaReceita.create(receita = bolo,
    ingrediente = xicoleo, quantidade = 1.0)

    # exibição padrão
    print(ing1.receita.nome, ing1.ingrediente.nome,ing1.ingrediente.unidade, ing1.quantidade)

    # listar receita e ingredientes
    for rec in Receita.select():
        print("=> "+rec.nome)
        ings = IngredienteDaReceita.select().where(IngredienteDaReceita.receita == rec)
        print("Ingredientes:")
        for ingrediente in ings:
            print(ingrediente.ingrediente.nome)
