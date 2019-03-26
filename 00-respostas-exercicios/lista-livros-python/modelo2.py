# programa similar ao modelo.py, porém:
# - criando a lista diretamente com objetos
# - usando método __str__ para exibir os objetos

class Livro:
    def __init__(self, titulo="", autores="", ano="", editora=""):
        self.titulo = titulo
        self.autores = autores
        self.ano = ano
        self.editora = editora
    def __str__(self):
        return self.titulo+", "+self.autores+", "+self.ano+", "

lista = [
    Livro("Programação em Python 3", "Mark Summerfield", "2013", "Alta Books"),
    Livro("Python para desenvolvedores", "Luiz Eduardo Borges", "2014", "Novatec")
    ]
for livro in lista:
    print(livro)