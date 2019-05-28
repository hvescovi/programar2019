import peewee, os

# conexão com o banco de dados do SQLLite
db = peewee.SqliteDatabase('animalia.db')

# declaração da classe herdando características da classe Model
class Animal(peewee.Model):
    # atributos do tipo texto
    nomedono = peewee.CharField()
    tipo_animal = peewee.CharField()
    raca = peewee.CharField()
    # subclasse que estabelece vínculo da classe com o banco de dados
    class Meta:
        # o atributo database se refere à variável de conexão com o BD
        database = db
    # o método __str__ agrega estilo de exibição de informações da classe
    def __str__(self):
        return self.tipo_animal+","+self.raca+" de "+self.nomedono

class Consulta(peewee.Model):
    data = peewee.CharField()
    servico = peewee.CharField()
    horario = peewee.CharField()
    # o atributo animal possui um valor que é uma instância de outra classe 
    animal = peewee.ForeignKeyField(Animal)
    confirma = peewee.CharField()
    myID = peewee.CharField()
    class Meta:
        database = db
    def __str__(self):
        # a contrabarra permite continuar a soma de strings
        return self.servico+" em "+self.data+":"+self.horario+", confirmado: "+\
        self.confirma+", ID da consulta: "+self.myID+" | animal: "+str(self.animal)

# teste das classes e da persistência
if __name__ == '__main__':
    # apagar o arquivo caso ele exista
    arq = 'animalia.db'
    if os.path.exists(arq):
        os.remove(arq)

    try:
        # conectar-se ao banco de dados
        db.connect()
        # solicitar a criação das tabelas
        db.create_tables([Animal,Consulta]) 
    # é preciso tratar erros    
    except peewee.OperationalError as e:
        print("erro ao criar tabelas: "+str(e))

    print("TESTE DO ANIMAL")
    # criar um animal
    a1 = Animal(nomedono="José", tipo_animal="C", raca="Chiuaua")
    print(a1)

    print("TESTE DA CONSULTA")
    # criar uma consulta
    c1 = Consulta(data="19/09/2018", servico="Consulta de rotina", 
    horario="14:00", animal=a1, confirma="N", myID="c9d8f7gu4h3hnwsik3e")
    print(c1)

    print("TESTE DA PERSISTÊNCIA")
    # salvar o chiuaua
    a1.save()
    # salvar a consulta
    c1.save()
    # criar uma nova consulta
    c2 = Consulta(data="21/09/2018", servico="Aplicação de vacina", 
    horario="10:00", animal=a1, confirma="S", myID="d9firtu3434uit")
    # salva a consulta
    c2.save()
    # obter todas as consultas
    todos = Consulta.select()
    # percorrer e mostrar as consultas
    for con in todos:
        print(con)    