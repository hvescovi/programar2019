import os
# o estilo de importação a seguir dispensa o uso da palavra peewee em comandos
from peewee import *

# conectar as classes ao banco de dados -----------------------------

# definir o nome do arquivo de dados do SQLite
arq = 'manytomany-estilo1.db'
# ligar o arquivo do SQLite com uma variável
db = SqliteDatabase(arq)
# definir classe-pai que utiliza ligação com BD (class Meta)
class BaseModel(Model):
    class Meta:
        database = db

# definir classes de modelo -----------------------------------------

class Aluno(BaseModel):
    nome = CharField()
    
class Disciplina(BaseModel):
    nome = CharField()

class AlunoDisciplina(BaseModel):
    aluno = ForeignKeyField(Aluno)
    disciplina = ForeignKeyField(Disciplina)

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
joao = Aluno.create(nome = "Joao da Silva")
ingles = Disciplina.create(nome = 'Inglês')
espanhol = Disciplina.create(nome = 'Espanhol')

# definir as disciplinas que Joao cursa
disciplina1Joao = AlunoDisciplina.create(aluno=joao, disciplina=ingles)
disciplina2Joao = AlunoDisciplina.create(aluno=joao, disciplina=espanhol)

maria = Aluno.create(nome = 'Maria')

# definir disciplinas que Maria cursa
disciplinaMaria = AlunoDisciplina.create(aluno=maria, disciplina=ingles)

# testar as classes: exibição de informações ------------------------

# listar quais disciplinas são cursadas por quais alunos
# obtém a lista de alunos & disciplinas
q1 = AlunoDisciplina.select()
print("Quais alunos cursam quais disciplinas:")
for dado in q1:
    print(dado.aluno.nome+" cursa: "+
    dado.disciplina.nome)