import os
from peewee import *

arq = 'many-to-many-com-lista.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db
        
class Aluno(BaseModel):
    nome = CharField()

class Disciplina(BaseModel):
    nome = CharField()
    # criar um campo do tipo varios-para-varios
    alunos = ManyToManyField(Aluno) 

# incializações
if os.path.exists(arq):
        os.remove(arq)
db.connect()
db.create_tables([
    Aluno,
    Disciplina,
    # deve-se solicitar a criação da tabela do relacionamento N x N
    # apesar de só haver 2 classes, uma tabela é necessária para armazenar os dados do relacionamento
    Disciplina.alunos.get_through_model()])

# criando objetos
joao = Aluno.create(nome = "Joao da Silva")
ingles = Disciplina.create(nome = 'Inglês')
espanhol = Disciplina.create(nome = 'Espanhol')

# informando que João cursa disciplinas de inglês e espanhol
# basta adicionar as disciplinas no aluno
# NÃO foi declarado na classe Aluno que o mesmo possui um atributo 'disciplinas'
# PORÉM, é feito o MAPEAMENTO REVERSO: se alunos estão em disciplinas, disciplinas possuem alunos
# é criado um atributo com o nome da classe relacionada, adicionado de um 's'
joao.disciplinas.add([ingles, espanhol])

# Maria cursa espanhol
maria = Aluno.create(nome = 'Maria')
espanhol.alunos.add(maria)

# listagem de informações
todos = Disciplina.select()
for disc in todos:
    print("Quem cursa a disciplina:"+disc.nome)
    for aluno in disc.alunos:
         print(aluno.nome)

# mostrando apenas disciplinas de Joao
print("Disciplinas de Joao:")
for disciplina in joao.disciplinas:
    print(disciplina.nome)