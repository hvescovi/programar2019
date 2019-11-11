# http://docs.peewee-orm.com/en/latest/peewee/models.html#model-options-and-table-metadata


import os
from peewee import *
import datetime

arq = "detalhes.db"
db = SqliteDatabase(arq)

# definir classe-pai que utiliza ligação com BD (class Meta)
class BaseModel(Model):
    class Meta:
        database = db

# definir classes de modelo -----------------------------------------

# toda classe deve herdar BaseModel, em vez de Model
# dessa forma, o atributo database da subclasse Meta já estará definido
class Aluno(BaseModel):
    nome = CharField()
    cpf = CharField(primary_key=True)
    email = CharField(unique=True, index=True)
    
class Disciplina(BaseModel):
    nome = CharField(unique=True)
    class Meta:
        table_name = "materia"

class AlunoDisciplina(BaseModel):
    aluno = ForeignKeyField(Aluno, column_name="cod_aluno")
    disciplina = ForeignKeyField(Disciplina, backref="materia")
    data_matricula = DateTimeField(default=datetime.datetime.now)
    class Meta:
        primary_key = CompositeKey('aluno', 'disciplina')

# teste das classes: inicializar BD ---------------------------------

# apagar arquivo de banco de dados, caso exista
if os.path.exists(arq):
    os.remove(arq)

# conectar-se ao BD e criar tabelas
db.connect()
db.create_tables([
    Aluno,
    Disciplina,
    AlunoDisciplina])

# criar instâncias de objetos ---------------------------------------

# ao usar o método "create", o objeto já é salvo (não é preciso usar o método "save")
joao = Aluno.create(nome = "Joao da Silva", cpf="123.456.789-10", email="jo@gmail.com")
ingles = Disciplina.create(nome = 'Inglês')
espanhol = Disciplina.create(nome = 'Espanhol')

# definir as disciplinas que Joao cursa
disciplina1Joao = AlunoDisciplina.create(aluno=joao, disciplina=ingles)
disciplina2Joao = AlunoDisciplina.create(aluno=joao, disciplina=espanhol)

maria = Aluno(nome = 'Maria', cpf="987.654.321-99", email="maria@gmail.com")
maria.save(force_insert=True)

# definir que Maria cursa inglês
disciplinaMaria = AlunoDisciplina.create(aluno=maria, disciplina=ingles)

# testar as classes: exibição de informações ------------------------

# listar quais disciplinas são cursadas por quais alunos
# obtém a lista de alunos & disciplinas
q1 = AlunoDisciplina.select()
print("Quais alunos cursam quais disciplinas:")
for dado in q1:
    print(dado.aluno.nome+" cursa: " + dado.disciplina.nome+", matrícula em:",dado.data_matricula)