from peewee import *
import os

arq = "PythonwithBD.db"
db = SqliteDatabase(arq)

class BaseModel(Model):

	class Meta:
		database = db

class Pessoa(BaseModel):

	def __init__(self, codigo, nome, endereco, telefone):
		self.codigo = codigo
		self.nome = nome
		self.endereco = endereco
		self.telefone = telefone

if __name__ == "__main__":

	if os.path.exists(arq):
		os.remove(arq)
	db.connect()
	db.create_tables([Pessoa])

# TESTE PARA VERIFICAR SE ESSE NEGÓCIO DE BRANCH FUNCIONA MESMO
'''UM NOVO TESTE TODOS OS DIAS, VAMOS VER SE DÁ'''